/*
Techincal University of Moldova
Lab No. 1. Computer Programming. C Language Basics.
Date 18.09.2021
Author: Cernega Vladislav
Lecuture: Dumitru Prijilevschi 
*/

#include <iostream>
#include <stack>
#include <math.h>
using namespace std;

const double Pi = acos(-1); 

double Sin(double x) { 
	return (round(sin(x) * 10000000) / 10000000);
}

double Cos(double x) { 
	return (round(cos(x) * 10000000) / 10000000);
}

double ctg(double x) { 
	double a = Cos(x);
	double b = Sin(x);
	return (a / b);
}

struct Digit 
{
	char type; 
	double value; 
};

bool Maths(stack <Digit>& Stack_n, stack <Digit>& Stack_o, Digit& item) { 
	double a, b, c;
	a = Stack_n.top().value;
	Stack_n.pop(); 
	switch (Stack_o.top().type) { 
	case '+': 
		b = Stack_n.top().value;
		Stack_n.pop();
		c = a + b;
		item.type = '0';
		item.value = c;
		Stack_n.push(item);
		Stack_o.pop();
		break;

	case '-':
		b = Stack_n.top().value;
		Stack_n.pop();
		c = b - a;
		item.type = '0';
		item.value = c;
		Stack_n.push(item);
		Stack_o.pop();
		break;

	case '^':
		b = Stack_n.top().value;
		Stack_n.pop();
		c = pow(b, a);
		item.type = '0';
		item.value = c;
		Stack_n.push(item);
		Stack_o.pop();
		break;

	case '*':
		b = Stack_n.top().value;
		Stack_n.pop();
		c = a * b;
		item.type = '0';
		item.value = c;
		Stack_n.push(item);
		Stack_o.pop();
		break;

	case '/':
		b = Stack_n.top().value;
		if (a == 0) {
			cerr << "\nError! Cannot divide for 0\n";
			return false;
		}
		else {
			Stack_n.pop();
			c = (b / a);
			item.type = '0';
			item.value = c;
			Stack_n.push(item);
			Stack_o.pop();
			break;
		}

	case 's':
		c = Sin(a);
		item.type = '0';
		item.value = c;
		Stack_n.push(item);
		Stack_o.pop();
		break;

	case 'c':
		c = Cos(a);
		item.type = '0';
		item.value = c;
		Stack_n.push(item);
		Stack_o.pop();
		break;

	case 't':
		if (Cos(a) == 0) {
			cerr << "\n Invalid argument for tangent function!\n";
			return false;
		}
		else {
			c = tan(a);
			item.type = '0';
			item.value = c;
			Stack_n.push(item);
			Stack_o.pop();
			break;
		}

	case 'g':
		if (Sin(a) == 0) {
			cerr << "\n Invalid argument for cotangent function!\n";
			return false;
		}
		else {
			c = ctg(a);
			item.type = '0';
			item.value = c;
			Stack_n.push(item);
			Stack_o.pop();
			break;
		}

	case 'e':
		c = exp(a);
		item.type = '0';
		item.value = c;
		Stack_n.push(item);
		Stack_o.pop();
		break;

	case 'a':
		c = abs(a);
		item.type = '0';
		item.value = c;
		Stack_n.push(item);
		Stack_o.pop();
		break;

	default:
		cerr << "\nError!\n";
		return false;
		break;
	}
	return true;
}

int getPriority(char Ch) {
	if (Ch == '+' || Ch == '-')return 1;
	if (Ch == '*' || Ch == '/')return 2;
	if (Ch == '^')return 3;	
	if (Ch == 's' || Ch == 'c' || Ch == 't' || Ch == 'g' || Ch == 'e' || Ch == 'a')return 4;
	else return 0;
}

int main()
{
	cout << "   To use Pi number enter 'p', to use e number enter 'exp(1)'\n";
	cout << "   Enter your expression: ";
	char Ch; 
	double value;
	bool flag = 1; 
	stack <Digit> Stack_n; 
	stack <Digit> Stack_o; 
	Digit item; 
	while (1) {
		Ch = cin.peek(); 
		if (Ch == '\n')
			break; 
		if (Ch == ' ') { 
			cin.ignore();
			continue;
		}
		if (Ch == 's' || Ch == 'c' || Ch == 't' || Ch == 'e' || Ch == 'a') { 
			char funcs[3]; 
			for (int i = 0; i < 3; i++) {
				Ch = cin.peek();
				funcs[i] = Ch;
				cin.ignore();
				flag = 1;
			}
			if (funcs[0] == 's' && funcs[1] == 'i' && funcs[2] == 'n') {
				item.type = 's';
				item.value = 0;
				Stack_o.push(item); 
				continue;
			}
			if (funcs[0] == 'c' && funcs[1] == 'o' && funcs[2] == 's') { 
				item.type = 'c';
				item.value = 0;
				Stack_o.push(item); 
				continue;
			}
			if (funcs[0] == 't' && funcs[1] == 'a' && funcs[2] == 'n') { 
				item.type = 't';
				item.value = 0;
				Stack_o.push(item);
				continue;
			}
			if (funcs[0] == 'c' && funcs[1] == 't' && funcs[2] == 'g') { 
				item.type = 'g';
				item.value = 0;
				Stack_o.push(item); 
				continue;
			}
			if (funcs[0] == 'e' && funcs[1] == 'x' && funcs[2] == 'p') { 
				item.type = 'e';
				item.value = 0;
				Stack_o.push(item); 
				continue;
			}
			if (funcs[0] == 'a' && funcs[1] == 'b' && funcs[2] == 's') { 
				item.type = 'a';
				item.value = 0;
				Stack_o.push(item); 
				continue;
			}
			flag=0;
		}
		if (Ch == 'p') { 
			item.type = '0';
			item.value = Pi;
			Stack_n.push(item); 
			flag = 0;
			cin.ignore();
			continue;
		}
		if ((Ch >= '0' && Ch <= '9') || (Ch == '-' && flag == 1)) { 
			cin >> value;
			item.type = '0';
			item.value = value;
			Stack_n.push(item);
			flag = 0;
			continue;
		}
		if (Ch == '+' || (Ch == '-' && flag == 0) || Ch == '*' || Ch == '/' || Ch == '^') { 
			if (Stack_o.size() == 0) { 
				item.type = Ch;
				item.value = 0;
				Stack_o.push(item);
				cin.ignore();
				continue;
			}
			if (Stack_o.size() != 0 && getPriority(Ch) > getPriority(Stack_o.top().type)) { 
				item.type = Ch;
				item.value = 0;
				Stack_o.push(item); 
				cin.ignore();
				continue;
			}
			if (Stack_o.size() != 0 && getPriority(Ch) <= getPriority(Stack_o.top().type)) {
				if (Maths(Stack_n, Stack_o, item) == false) { 
					system("pause");
					return 0;
				}
				continue;
			}
		}
		if (Ch == '(') {
			item.type = Ch;
			item.value = 0;
			Stack_o.push(item);
			cin.ignore();
			continue;
		}
		if (Ch == ')') { 
			while (Stack_o.top().type != '(') {
				if (Maths(Stack_n, Stack_o, item) == false) { 
					system("pause");
					return 0;
				}
				else continue; 
			}
			Stack_o.pop();
			cin.ignore();
			continue;
		}
		else { 
			cout << "\nExpresia a fost introdusa gresit!\n";
			system("pause");
			return 0;
		}
	}
	while (Stack_o.size() != 0) { 
		if (Maths(Stack_n, Stack_o, item) == false) { 
			system("pause");
			return 0;
		}
		else continue; 
	}
	cout << "   Raspuns: " << Stack_n.top().value << endl;
	return 0;
}