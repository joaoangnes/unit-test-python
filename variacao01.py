from collections import Counter, defaultdict


class UtilitariosAnaliseTexto:
    def frequencia_palavras(self):
        """Retorna a frequência de cada palavra em um dicionário, ignorando maiúsculas/minúsculas."""
        palavras = self.texto.lower().split()
        return dict(Counter(palavras))

    def encontrar_frases_palindromas(self):
        pass

    def grupos_anagramas(self, lista_palavras):
        """Agrupa palavras que são anagramas entre si em uma lista de listas."""
        dicionario_anagramas = defaultdict(list)
        for palavra in lista_palavras:
            palavra_ordenada = ''.join(sorted(palavra.lower()))
            dicionario_anagramas[palavra_ordenada].append(palavra)
        return list(dicionario_anagramas.values())

    def prefixo_comum(self, lista_palavras):
        pass

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

    def contar_frases(self):
        pass

    def palavras_unicas_ordenadas(self):
        pass
