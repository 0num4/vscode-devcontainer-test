#include <iostream>
#include "sample.pb.h"

int main() {
  Person person;
  person.set_name("Alice");
  person.set_id(123);
  person.set_email("alice@example.com");

  std::cout << "Name: " << person.name() << std::endl;
  std::cout << "ID: " << person.id() << std::endl;
  std::cout << "Email: " << person.email() << std::endl;

  return 0;
}