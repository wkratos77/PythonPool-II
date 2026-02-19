from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)
        if not card1 or not card2:
            raise ValueError("One or both cards not found")

        if card1.rating > card2.rating:
            winner = card1
            loser = card2
        elif card2.rating > card1.rating:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            'winner': winner.name,
            'loser': loser.name,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        lb = sorted(self.cards.values(), key=lambda x: x.rating, reverse=True)
        return [
            f"{i+1}. {c.name} - Rating: {c.rating} ({c.wins}-{c.losses})"
            for i, c in enumerate(lb)]

    def generate_tournament_report(self) -> dict:
        ratings = [c.rating for c in self.cards.values()]
        avg = sum(ratings) / len(ratings) if ratings else 0
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": int(avg) if avg == int(avg) else round(avg, 1),
            "platform_status": "active" if self.matches_played > 0
            else "inactive"
        }
