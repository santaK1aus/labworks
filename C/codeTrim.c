#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#define MAX 20  //Buffer Size

void main(){
    FILE* fptr = fopen("codeTrim.c","r"); //Open file
    if(fptr == NULL){
        printf("File cannot be opened.");
        exit(0);
    }
    
    int lnum = 0, cnum = 0, cnet = 0;//linenumber, current character number, net no. of characters
    char buff[2][MAX];//array of buffers
    char lch = ' ';//last non-space character
    int str = 0, chr=0, sp = 0, comm = 0, end = 0;//str: ongoing string, chr: ongoing character, sp: space encountered, comm: ongoing comment, end: buffers left till end
    int bnum = 0, bnumo = 1;//buffer number
    if(fgets(buff[0], MAX, fptr)!=NULL)//load first buffer
        end++;//increase end to signify no. of available buffers
    if(fgets(buff[1], MAX, fptr)!=NULL)//load second buffer
        end++;
    while(end--){
        for(int i=0;i<MAX-1;i++){// NOTE : fgets loads till 2nd last element in array
            char nch = buff[bnum][i];//current character
            if(nch=='\n'){//if newline, set strings and chars to 0
                comm = 0;
                str = chr = 0;
                lnum++;
                if(lch!=' ')//print newline only if some other token was encountered
                    printf("\n");
                lch = ' ';
                break;
            }
            if(nch =='/' && ((i+1 < MAX-1 && buff[bnum][i+1]=='/')||(i+1>=MAX-1 && buff[bnumo][0] == '/')) && str!=1)//comment check across buffer
                comm = 1;
            if(comm == 1 && nch!='\n')//ongoing comment check
                continue;

            cnum++;//Valid char for compiler
            if(nch == '\"' && chr == 0)//string commence
                str = (str == 0)? 1 : 0;
            if(nch == '\'' && str == 0)//character commence
                chr = (chr == 0)? 1 : 0;
            if(nch == ' ' && str!=1 && chr!=1){//space encountered but string is not ongoing
                sp = 1;
            }
            else{//if not space or string is ongoing
                if(sp==1 && !(ispunct(nch) || ispunct(lch)) && lch!=' '){//if space was encountered in between and (both are non alphanumeric)
                    printf(" ");
                }
                printf("%c",nch);//print current char
                sp=0;//set space to 0 upon printing char
            }
            if(nch!=' ') lch=nch;//set non-space character as last character
        }
        cnet+=cnum;
        cnum=0;
        int t = bnum;//swap active buffers
        bnum = bnumo;
        bnumo = t;
        if(fgets(buff[bnumo], MAX, fptr)!=NULL)
            end++;//reload secondary buffer
    }
    printf("\nTotal lines : %d\nTotal Compilable chars : %d\n",lnum, cnet);
}
