//#include <iostream>

#ifndef checkf
#define checkf
#include <fstream>
//check multiple file
//return 0 kalo semua ada
int check_file(const char file[])
{
 std::ifstream check(file);
 return check.is_open();
}
/* kalo bisa
int check_fol(const char folder[])
{
}
*/


/*
int main(int args, char* argv[])
{
 if (args > 1)
 {
 int ada = 1;
 for (int i = 1; i < args; i++)
 {
  int hasil = ::check_file(argv[i]);
  //std::cout << hasil << std::endl;
  if (!hasil)
  {ada = 0;}
 }
 if (ada){return 0;}
 }
 else
 {
  std::cout << "Check file by Kevin Agusto. Written in C++\nplease input the file as program arguments :v\n";
 }
}
*/
#endif
