#include <stdio.h>

int main(int argc, const char *argv[]) {

  char c;
  printf("Press any key and then press Enter: \n");
  
  printf("You pressed: \n");
  c = getchar();
  putchar(c);
  putchar('\n');

  return 0;
}
