#include <math.h>
#include <stdio.h>

float calcular_area_circunferencia(float raio){
    return M_PI * raio;
}

/*
    Um vetor é um array de float com tamanho 2, onde o index 0 
    representa a componente i do vetor, e o index 1 representa
    a componente j.
*/
float* criar_vetor(float xf, float yf, float xi=0, float yi=0){
    float* vetor = new float[2]; 
    *(vetor) = xf-xi;
    *(vetor+1) = yf-yi;

    return vetor;
}

float calcular_modulo_vetor(float* vetor){
    return sqrt(vetor[0]*vetor[0] + vetor[1]+vetor[1]);
}

// Soma ao vetor1 o vetor2 - Nenhum vetor novo é gerado!
void somar_vetores(float* vetor1, float* vetor2){
    vetor1[0] += vetor2[0];
    vetor1[1] += vetor2[1];
}

/*
    Multiplicação de vetor por um escalar - Nenhum vetor novo é gerado. 
    Os dados modificam o vetor passado para a função!
*/
void multiplicar_vetor_escalar(float* vetor, float escalar){
    vetor[0] *= escalar; 
    vetor[1] *= escalar;
}

void exibir_vetor(float* vetor){
    printf("Vetor(%f,%f)", vetor[0], vetor[1]);
}

void movimentar_corpo(float* vetor_posicao, float* vetor_velocidade, int tempo=1){
    vetor_posicao[0] += vetor_velocidade[0] * tempo;
    vetor_posicao[1] += vetor_velocidade[1] * tempo;
}

// Verifica a colisão por meio da intersecção de circunferências
bool verificar_colisao(float* vetor_posicao1, float* vetor_posicao2, float raio1, float raio2){
    float xi = vetor_posicao1[0];
    float xf = vetor_posicao2[0];
    float yi = vetor_posicao1[1];
    float yf = vetor_posicao2[1];

    float* vetor_distancia = criar_vetor(xf, yf, xi, yi);

    if (calcular_modulo_vetor(vetor_distancia) <= (raio1 + raio2))
        return true;
    
    return false;
}