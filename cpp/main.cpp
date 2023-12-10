#include <iostream>
#include "mahjongsoul.pb.h"
#include <vector>

int main() {
//   Person person;
//   person.set_name("Alice");
//   person.set_id(123);
//   person.set_email("alice@example.com");

//   std::cout << "Name: " << person.name() << std::endl;
//   std::cout << "ID: " << person.id() << std::endl;
//   std::cout << "Email: " << person.email() << std::endl;
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    int sum = 0;

    for (int i = 0; i < numbers.size(); ++i) {
        sum += numbers[i];
        std::cout << "現在の合計: " << sum << std::endl;
    }

    std::cout << "最終合計: " << sum << std::endl;
    return 0;

  return 0;
}