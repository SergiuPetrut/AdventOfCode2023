#include <cmath>
#include <cstddef>
#include <exception>
#include <fstream>
#include <iostream>
#include <regex>
#include <string>

std::string nums[10] = {"zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
std::string nums_int[10] = {"0","1", "2", "3", "4", "5", "6", "7", "8", "9"};


bool myreplace(std::string &str, const std::string& from, const std::string& to){

  size_t start_pos = str.find(from);
  if (start_pos == std::string::npos) {
    return false;
  }
str.replace(start_pos, from.length(), to);
return true;
}





int firstDigit(int num);
int lastDigit(int num);
int firstDigit(int num) {

  int digits = (int)log10(num);
  num = (int)(num / pow(10, digits));
  return num;
}

int lastDigit(int num) { return num % 10; }

int main() {

  /*How to solve the puzzle :
   Step 1 : Get file data
   Step 2 : Remove all non-numbers (maybe regex?)
   Step 3 : Add first and last digit. Note : if the number is only 1 digit, that
   gets doubled. So if the line only has a 7, the output is 77. Step 4 :
   Finally, sum all numbers for the answer.
   */

  std::ifstream input(
      "input"); // create a ifstream object tie the object to the actual file
  std::string line;        // each line of the file
  std::string output_line; // line after being regex'd
  int output_int;
  long long int sum = 0;
  if (input.is_open()) {   // checks whether the file is open
    while (!input.eof()) { // While not hitting the end of the file 

      std::getline(input, line); // Get each line from the file
      for (int j=10;j>0;j--){
      for (int i = 10 ; i>=0; i--) {
        myreplace(line,nums[i],nums_int[i]);
      }
      }
      // std::cout<<line<<std::endl;
      output_line =
          std::regex_replace(line, std::regex(R"([\D])"),
                             ""); // Regex black magic!! (Remove everything that
                                  // is non - numerical)

      try {
        output_int = std::stoi(output_line); // tries to convert
      } catch (std::exception &err) { //if conversion unsuccesful
        output_int = 0; //just default output to 0
      }
      std::cout<<output_line<<std::endl;
      output_int = 10 * firstDigit(output_int) + lastDigit(output_int); //forms a new 2 digit number from the first and last characters
      // std::cout<<output_int<<std::endl;
      sum += output_int; // adds all the aforementioned double digit numbers together
    }
  }

  else {

    std::cout << "Can't open file!" << std::endl;
  }
  std::cout << sum << std::endl;
  return 0;
}
