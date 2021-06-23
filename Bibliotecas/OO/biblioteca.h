#include <iostream>
#include <math.h>
#include <stdio.h>

class Vetor {

    /*
        Classe para representar um vetor no Plano Cartesiano

        Pode ser usada para expressar a Posição e Velocidade de um Corpo
    */

    public:

        float x;
        float y;

        Vetor():
            x(0), y(0){
        }

        Vetor(float xf, float yf, float xi=0, float yi=0):
            x(xf-xi), y(yf-yi){
        }

        float getModulo(){
            return  sqrt(x*x + y*y);
        }

        /* Sobrecarga de operadores */

        // Operador para saída de dados
        friend std::ostream& operator<< (std::ostream &out, const Vetor &vetor){
            out << "Vetor(" << vetor.x << "," << vetor.y << ")";
            return out;
        }

        // Operador de Soma
        Vetor operator+(const Vetor &vetor){
		    return Vetor(x + vetor.x, y + vetor.y);
	    }

        // Operador de Subtração
        Vetor operator-(const Vetor &vetor){
		    return Vetor(x - vetor.x, y - vetor.y);
	    }

        // Multiplicação de um Vetor por um escalar a esquerda
        friend Vetor operator*(const float escalar, const Vetor &vetor){
		    return Vetor(vetor.x * escalar, vetor.y * escalar);
	    }

        // Multiplicação de um Vetor por um escalar a direita
        friend Vetor operator*(const Vetor &vetor, const float escalar){
		    return Vetor(vetor.x * escalar, vetor.y * escalar);
	    }

};

class Circunferencia {

    /*
        Classe para representar um circunferência.

        Pode ser usado para definir o formato que um corpo físico
        possui na simulação para fins de cálculo de colisão entre
        corpos.
    */

    public:

        float centro_x;
        float centro_y;
        float raio;

        Circunferencia():
            centro_x(0), centro_y(0), raio(0){
        }

        Circunferencia(float cx, float cy, float raio):
            centro_x(cx), centro_y(cy), raio(raio){
        }

        float getArea(){
            return M_PI * raio;
        }

};

class Corpo {

    /*
        Classe para representar um corpo físico na simulação. Um corpo
        possui uma posição no espaço, um vetor velocidade, uma valor de massa
        e um formato - Nesse caso somente são aceitas circunferências.

        Através da posição, velocidade é possível movimentar o corpo em uma 
        unidade de tempo.
    */

    public:

        Vetor posicao;
        Vetor velocidade;
        float massa;
        Circunferencia formato;

        Corpo():
            posicao(Vetor()), velocidade(Vetor()), massa(0), formato(Circunferencia()){
        }

        Corpo(Vetor p, Vetor v, float m, float r):
            posicao(p), velocidade(v), massa(m)
        {
            formato = Circunferencia(posicao.x, posicao.y, r);
        }

        void movimentar(int tempo=1){
            posicao = posicao + velocidade * tempo;
        }

        // Verifica colisão por meio da intersecção de duas circunferências
        bool verificar_colisao(const Corpo &corpo){
            Vetor distancia = Vetor(posicao.x, posicao.y, corpo.posicao.x, corpo.posicao.y);

            if (distancia.getModulo() <= (formato.raio + corpo.formato.raio))
                return true;

            return false;
        }

        // Sobrecarga do operador de saída de dados
        friend std::ostream& operator<< (std::ostream &out, const Corpo &corpo){
            out << "Massa: " << corpo.massa << "\n"
                << "Raio Circunferencia: " << corpo.formato.raio << "\n"
                << "Vetor Posicao: " << corpo.posicao << "\n"
                << "Vetor Velocidade: " << corpo.velocidade;

            return out;
        }

};