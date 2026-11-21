class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i: int) -> bool:
            # Siamo arrivati esattamente alla fine di s: segmentazione riuscita
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for word in wordDict:
                # Controlla se s a partire dall'indice i inizia con l'intera parola
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True

            # Nessuna parola da i ha portato a una soluzione valida
            memo[i] = False
            return False

        return dfs(0)