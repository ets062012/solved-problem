class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_count = {}
        loss_count = {}

        for winner, loser in matches:
            if winner in win_count:
                win_count[winner] += 1
            else:
                win_count[winner] = 1

            if loser in loss_count:
                loss_count[loser] += 1
            else:
                loss_count[loser] = 1

        players_no_losses = [player for player in win_count if player not in loss_count]
        players_one_loss = [player for player in loss_count if loss_count[player] == 1]

        return [sorted(players_no_losses), sorted(players_one_loss)]
        