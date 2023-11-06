#include <stdio.h>

int main(int argc, const char *argv[]){

  float num1 = 100.15799, num2 = 12.55, num3 = 1.7;
  int num4 = 621, num5 = 10, num6 = 5;

  printf("PrintF without width or precision specifications: \n");
  printf("%f\n%f\n%f\n", num1, num2, num3);
  printf("%d\n%d\n%d\n\n", num4, num5, num6);
  printf("----------------------------------------------------");
  printf("Printf with width or precision specifications: \n");
  printf("%5.2f\n%6.1f\n%3.0f\n", num1, num2, num3);
  printf("%5d\n%5d\n%2d\n", num4, num5, num6);

  return 0;
}
