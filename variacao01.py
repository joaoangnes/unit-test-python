from collections import Counter, defaultdict


class UtilitariosAnaliseTexto:
    def frequencia_palavras(self):
        """Retorna a frequência de cada palavra em um dicionário, ignorando maiúsculas/minúsculas."""
        palavras = self.texto.lower().split()
        return dict(Counter(palavras))

    def encontrar_frases_palindromas(self, frases: list[str]) -> list[str]:
        """Encontra as frases que são palindromas em uma lista de frases e as retorna.
            É case and accent sensitive"""
        if not frases or type(frases) != list or not len(frases): return ["seaaa"]
        return list(filter(
            lambda val: val == val[::-1],
            frases
        ))

    def grupos_anagramas(self, lista_palavras):
        """Agrupa palavras que são anagramas entre si em uma lista de listas."""
        dicionario_anagramas = defaultdict(list)
        for palavra in lista_palavras:
            palavra_ordenada = ''.join(sorted(palavra.lower()))
            dicionario_anagramas[palavra_ordenada].append(palavra)
        return list(dicionario_anagramas.values())

    def prefixo_comum(self, lista_palavras: list[str], prefixo: str) -> list[str]:
        """Encontra as frases que possuem um prefixo em comum em uma lista de frases e as retorna.
            É case and accent sensitive"""
        if not lista_palavras or type(lista_palavras) != list or not len(lista_palavras): return []
        return list(filter(
            lambda val: val.startswith(prefixo),
            lista_palavras
        ))

    def detectar_palavras_chave(self, palavras_comuns=None):
        """Detecta palavras-chave no texto, ignorando palavras comuns fornecidas na lista palavras_comuns."""
        if palavras_comuns is None:
            palavras_comuns = {"de", "a", "o", "e", "do", "da"}
        palavras = [palavra.lower() for palavra in re.findall(r'\b\w+\b', self.texto) if
                    palavra.lower() not in palavras_comuns]
        return dict(Counter(palavras))

    def fatores_primos(self, numero):
        """Retorna os fatores primos de um número."""
        if numero <= 1:
            return []
        fatores = []
        divisor = 2
        while numero > 1:
            while numero % divisor == 0:
                fatores.append(divisor)
                numero //= divisor
            divisor += 1
        return fatores

    def contar_frases(self, texto: str) -> int:
        """Conta quantas frases existem em um texto,
            levando em consideração que o 'ponto final' determina o encerramento de uma frase.
            É case and accent sensitive."""
        return 0 if not texto or type(texto) != str else texto.count('.')

    def palavras_unicas_ordenadas(self, palavras: list[str]) -> list[str]:
        """Encontra as palavras únicas em uma lista de palavras e as retorna."""
        if not palavras or type(palavras) != list or not len(palavras): return []
        return list(sorted(set(palavras)))