#include <stdio.h>

int main(int argc, char *argv[]) {
  
  float temperatureFahrenheit;
  printf("Enter a temperature in degrees Fahrenheit: \n");
  scanf("%f", &temperatureFahrenheit);
  printf("Converting temperature to Celsius... \n");
  printf("Temperature (%f)F == (%f)C \n", temperatureFahrenheit, (temperatureFahrenheit-32.0)*(5.0/9.0));

  return 0;
}
