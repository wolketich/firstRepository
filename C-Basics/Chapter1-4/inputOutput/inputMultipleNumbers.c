#include <stdio.h>

int main(int argc, char *argv[])
{
  float sum;
  float num1, num2;

  printf("Type 2 numbers; press Enter after each number. \n");
  scanf("%f", &num1);
  scanf("%f", &num2);

  sum = num1 + num2;

  printf("%5.2f plus %6.2f is %6.2f. \n", num1, num2, sum);

  return 0;
}
