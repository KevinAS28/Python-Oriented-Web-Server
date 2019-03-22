#ifndef OWS_BACKUP
#define OWS_BACKUP
#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <sstream>
std::string ext = ".OWS_BACKUP";
std::string waktu()
{
 int waktu = time(NULL);
 std::stringstream obj;
 std::string hasil;
 obj << waktu;
 obj >> hasil;
 return hasil;
}
std::string cek(std::string file)
{
 //cek dulu di OWS_BACKUP
 std::string backup_folder = "OWS_BACKUP/";
 std::fstream coba(backup_folder+file, std::ios::in);
 if (coba.is_open()){return "bisa";}
 else {return "ngak";}
}
int backup(std::string file)
{
 //read dulu
 std::fstream baca(file, std::ios::binary|std::ios::in);
 baca.seekg(0, std::ios::end);
 int count = baca.tellg();
 char *hasil0 = NULL;
 hasil0 = new char[count];
 baca.seekg(0, std::ios::beg);
 baca.read(hasil0, count);
 //write
 std::string nama  = "OWS_PAGE/" + file + "_" + waktu() + ext;
 std::fstream tulis(nama, std::ios::binary|std::ios::out);
 tulis.write(hasil0, count);
 baca.close();tulis.close();
 delete []hasil0;
}
#endif
