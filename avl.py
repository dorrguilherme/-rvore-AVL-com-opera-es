# Codigo realizado para atividade de Algoritmos e Programação: Árvores e Ordenação
# Módulo 2 - Resposta ao desafio
# Desenvolvido por Guilherme Mathias Dörr

# Implementar uma árvore AVL com operações de inserção exclusão e busca.
# Chaves inteiras;       Entradas realizadas via teclado;
# Saida realizada com impressão;     Operação de rotação e motivo devem ser impressos;

class No:
    # inicialização de nó
    def __init__(self, valor):
        self.chave = valor;
        self.esquerda = None;
        self.direita = None;
        self.altura = 1;


class Arvore:
    # inicialização da árvore
    def __init__(self):
        self.raiz = None

    # metodo para calculo de altura
    def altura(self, no):
        if no is None:
            return 0;
        return no.altura;

    # metodo para balanceamento de no
    def balancemento(self, no):
        if no is None:
            return 0;
        return self.altura(no.esquerda) - self.altura(no.direita);

    def rotacaoDireita(self, no):
        # armazena valores de no antigo e define como raiz
        novaRaiz = no.esquerda;
        subarvoreDireita = novaRaiz.direita;

        # realiza a rotação
        novaRaiz.direita = no;
        no.esquerda = subarvoreDireita;

        # atualiza a altura
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita));
        novaRaiz.altura = 1 + max(self.altura(novaRaiz.esquerda), self.altura(novaRaiz.direita));

        # retorno da nova raiz da subarvore
        return novaRaiz;

    def rotacaoEsquerda(self, no):
        novaRaiz = no.direita;
        subarvoreEsquerda = novaRaiz.esquerda;

        novaRaiz.esquerda = no;
        no.direita = subarvoreEsquerda;

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita));
        novaRaiz.altura = 1 + max(self.altura(novaRaiz.esquerda), self.altura(novaRaiz.direita));

        return novaRaiz;

#    def inserir(self, valor):
#        if self.raiz is None:
#            self.raiz = No(valor);
#        else:
#            self.raiz = self.insere(self.raiz, valor);

    def insere(self, raiz, valor):
        # Caso seja um Nó inicial, insere
        if raiz is None:
            return No(valor);

        # Define local de inserção de acordo com as regras de arvore AVL
        if valor < raiz.valor:
            raiz.esquerda = self.insere(raiz.esquerda, valor);
        else:
            raiz.direita = self.insere(raiz.direita, valor);

        # Armazena a altura do nó
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita));

        # Verifica balanceamento
        fatorBalanceamento = self.balancemento(raiz);

        if fatorBalanceamento > 1:
            if valor < raiz.esquerda.valor:
                return self.rotacaoDireita(raiz);
            else:
                raiz.esquerda = self.rotacaoEsquerda(raiz.esquerda);
                return self.rotacaoDireita(raiz);

        elif fatorBalanceamento < -1:
            if valor > raiz.direita.valor:
                return self.rotacaoEsquerda(raiz);
            else:
                raiz.direita = self.rotacaoDireita(raiz.direita);
                return self.rotacaoEsquerda(raiz);

        return raiz;

    def imprime(self):
        if self.raiz is None:
            print("Árvore vazia");
        else:
            print("Árvore AVL:");
            self.imprimeArvore(self.raiz);

    def imprimeArvore(self, raiz):
        if raiz.esquerda is not None:
            self.imprimeArvore(raiz.esquerda);

        print(f"{raiz.chave} (altura: {raiz}");

        if raiz.direita is not None:
            self.imprimeArvore(raiz.direita);


#
#
#       CÓDIGO PRINCIPAL: Execução da rotina
#
#

arvore = Arvore();
arvore.imprime();

R = arvore.insere(arvore.raiz, 1);

arvore.imprime();
