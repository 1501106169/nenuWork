//create.cpp
#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main(int argc, char* argv[])
{
	if (argc != 2) { return 0; }
	int num = atoi(argv[1]);        //ÊäÈëÐÎÊ½create 100 > file

	srand((unsigned)time(NULL));
	for (int i = 0; i < num; i++)
	{
		cout << rand() << "\n";
	}
	cout << endl;
	return 0;
}