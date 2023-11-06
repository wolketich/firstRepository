//
//  simpleOutput.c
//  C-Basics
//
//  Created by Vladislav Cernega on 06/11/2023.
//

#include <stdio.h>

int simple_output(int argc, char *const argv[]) {
    
    int v1;
    float v2;
    char v3;
    
    v1 = 65;
    v2 = -18.23;
    v3 = 'a';
    
    printf("v1 hast the value %d. \n", v1);
    printf("v2 hast the value %f. \n", v2);
    printf("v3 hast the value %c. \n", v3);
    
    
    return 0;
}
