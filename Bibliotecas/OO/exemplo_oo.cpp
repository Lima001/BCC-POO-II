#include <iostream>
#include "biblioteca.h"

int main(){
    
    // Dados Corpo 1
    Corpo c1 = Corpo(Vetor(-60,0), Vetor(10,0), 50, 2);

    // Dados Corpo 2
    Corpo c2 = Corpo(c1.posicao * -1, c1.velocidade * -1, 10, 2);

    // Array com objetos da classe Corpo
    Corpo array_corpos[2] = {c1, c2};

    // Exibindo os objetos usando sobrescrita do operador <<
    for (int i=0; i<2; i++){
        std::cout << "Objeto: " << i << std::endl;
        std::cout << array_corpos[i] << std::endl;
    }

    std::cout << std::endl;;

    // Simulação de tempo - Variação em 10 unidades
    for (int i=1; i<=10; i++){
        std::cout << "TEMPO " << i << std::endl << std::endl;

        // Movimentando cada Corpo e exibindo sua posição
        for (int i=0; i<2; i++){
            std::cout << "Objeto: " << i << std::endl;
            array_corpos[i].movimentar();
            std::cout << array_corpos[i] << std::endl;
        }

        // Verificando se os corpos listados colidiram
        for (int i=0; i<2; i++){
            
            for (int j=i+1; j<2; j++){
                // Se colidiram, invertemos sua velocidade - Os corpos movimentam-se para direção contrária
                if (array_corpos[i].verificar_colisao(array_corpos[j])){
                    array_corpos[i].velocidade = array_corpos[i].velocidade * -1;
                    array_corpos[i].velocidade = array_corpos[i].velocidade * -1; 
                }
            }
        }

        std::cout << std::endl;
    }

    std::cout << std::endl;

    // Exibindo dados dos Corpos criados após execução do movimento
    for (int i=0; i<2; i++){
        std::cout << "Objeto: " << i << std::endl;
        std::cout << array_corpos[i] << std::endl;
    }

    return 0;
    
}