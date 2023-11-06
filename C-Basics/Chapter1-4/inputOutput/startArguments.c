#include <stdio.h>

int main(int argc, char *argv[]) {
  
  // Display arguments count
  printf("Arguments count - %d \n", argc);
  
  // Display arguments
  int i = 0;
  while (i < 150) {
    i++;
    if (argv[i] == '\0') break;
    printf("%c", argv[i]);
  };

  printf("\n");
  

  return 0;
}
