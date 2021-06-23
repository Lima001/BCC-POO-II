#include "biblioteca.h"
#include <iostream>

int main(){
    
    // Dados do Corpo 1
    float* vetor_velocidade_1 = criar_vetor(10, 0);
    float* vetor_posicao_1 = criar_vetor(-60, 0);
    float raio_1 = 2;
    float massa_1 = 50;

    // Dados do Corpo 2
    float* vetor_velocidade_2 = criar_vetor(10, 0);
    float* vetor_posicao_2 = criar_vetor(-60, 0);
    
    multiplicar_vetor_escalar(vetor_velocidade_2, -1);
    multiplicar_vetor_escalar(vetor_posicao_2, -1);
    
    float raio_2 = 2;
    float massa_2 = 10;

    // Array com os dados do raio de cada objeto, seguindo a ordem do array anterior
    float lista_raio_corpos[2] = {raio_1, raio_2};

    // Array com os dados vetoriais de cada corpo - (Posição, Velocidade)
    float* lista_vetores_corpos[2][3] = {
        {vetor_posicao_1, vetor_velocidade_1}, 
        {vetor_posicao_2, vetor_velocidade_2}, 
    };

    // Exibindo dados dos Corpos criados com a função exibir_vetor()
    for (int i=0; i<2; i++){
        std::cout << "Objeto " << i << " - ";
        exibir_vetor(lista_vetores_corpos[i][0]);
        std::cout << " / ";
        exibir_vetor(lista_vetores_corpos[i][1]);
        std::cout << std::endl;
    }

    std::cout << std::endl;
    
    // Simulação de tempo - Variação em 10 unidades
    for (int tempo=1; tempo<=10; tempo++){
        std::cout << "TEMPO: " << tempo << std::endl;
        
        // Movimentando cada Corpo e exibindo sua posição
        for (int i=0; i<2; i++){
            movimentar_corpo(lista_vetores_corpos[i][0], lista_vetores_corpos[i][1]);
            std::cout << i << " - ";
            exibir_vetor(lista_vetores_corpos[i][0]);
            std::cout << std::endl;
        }

        // Verificando se os corpos listados colidiram
        for (int i=0; i<2; i++){
            
            for (int j=i+1; j<2; j++){
                // Se colidiram, invertemos sua velocidade - Os corpos movimentam-se para direção contrária
                if (verificar_colisao(
                        lista_vetores_corpos[i][0],
                        lista_vetores_corpos[j][0],
                        lista_raio_corpos[i],
                        lista_raio_corpos[j]))
                    {
                        multiplicar_vetor_escalar(lista_vetores_corpos[i][1], -1);
                        multiplicar_vetor_escalar(lista_vetores_corpos[j][1], -1);
                }
            }
        }

        std::cout << std::endl;
    }

    std::cout << std::endl;

    // Exibindo dados dos Corpos criados após execução do movimento
    for (int i=0; i<2; i++){
        std::cout << "Objeto " << i << " - ";
        exibir_vetor(lista_vetores_corpos[i][0]);
        std::cout << " / ";
        exibir_vetor(lista_vetores_corpos[i][1]);
        std::cout << std::endl;
    }

    // Liberando memória dinamica alocada para os vetores
    for (int i=0; i<2; i++){
            delete[] lista_vetores_corpos[i][0];
            delete[] lista_vetores_corpos[i][1];
        }

    return 0;
}