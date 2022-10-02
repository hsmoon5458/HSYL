#include <iostream>
#define testMacro(input_var)\
std::cout << input_var << std::endl;\

int main(){
    std::cout << "Hello world!" << std::endl;
    testMacro(3);
    system("pause");
    return 0;
}
