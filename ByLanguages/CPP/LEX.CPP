#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<stdlib.h>
#include<ctype.h>
char key[5][8] = {"int","float","char","long","double"};
class lex
{
private:
	char string[101];
	int length,pointer;
public:
	lex()
	{
		strcpy(string," ");
		length = strlen(string);
		pointer = 0;
	}
	lex(char *temp)
	{
		strcpy(string,temp);
		length = strlen(string);
		pointer = 0;
	}
	void stringin()
	{
		cout<<"Enter A String : ";
		gets(string);
		length = strlen(string);
		pointer = 0;
	}
	void stringout()
	{
		cout<<"The String Entered is : "<<string<<endl;
		cout<<"The Length of String is : "<<length<<endl;
	}
	void strvalid()
	{
		int x,comma,i;
		x = 0; comma = 0; i = 0;
		if(string[length-1]!=';')
		{
			cout<<"String is not valid."<<endl;
			getch();
			exit(0);
		}
		x = key_che();
		if(!x)
		{
			cout<<"String is not valid."<<endl;
			getch();
			exit(0);
		}
		comma = countcomma();
		for(i=0;i<=comma;i++)
		{
			x = ide_che();
			if(!x)
			{
				cout<<"String is not valid."<<endl;
				getch();
				exit(0);
			}
		}
		cout<<"String is valid."<<endl;
	}
	int countcomma()
	{
		int i,comma;
		i = 0;comma = 0;
		while(i<length)
		{
			if(string[i]==',')
			{
				comma++;
			}
			i++;
		}
		return comma;
	}
	int key_che()
	{
		int i,j,z;
		char temp1[101];
		i=0;
		j=0;
		z=0;
		while(string[i]!= ' ')
		{
			temp1[i] = string[i];
			i++;
		}
		temp1[i]='\0';
		i++;
		pointer = i;
		for(j=0;j<5;j++)
		{
			if(strcmp(temp1,key[j])==0)
			{
				z = 1;
				break;
			}
		}
		if(z==1)
		{
			cout<<"The Keyword Entered is a Valid One"<<endl;
			return z;
		}
		else
		{
			cout<<"The Keyword Entered is not a Valid One"<<endl;
			return z;
		}
	}
	int ide_che()
	{
		int i,j,z,c;
		char temp2[101];
		i = pointer;
		j = 0;
		while(string[i]!=','&&string[i]!=';')
		{
			temp2[j] = string[i];
			i++;
			j++;
		}
		temp2[j]='\0';
		i++;
		pointer = i;
		j = 0;
		z = 0;
		c = temp2[j];
		if(isalpha(c))
		{
			j++;
			while(temp2[j]!='\0')
			{
				c = temp2[j];
				if(!isalpha(c))
				{
					if(!isdigit(c))
					{
						if(temp2[j]!='_')
						{
							z = 1;
							break;
						}
					}
				}
				j++;
			}
		}
		else
		{
			z = 1;
		}
		if(z==0)
		{
			cout<<"The Identifier is a Valid One"<<endl;
			return 1;
		}
		else
		{
			cout<<"The Identifier is not a Valid One"<<endl;
			return 0;
		}
	}
}
main()
{
	lex s1;
	clrscr();
	s1.stringin();
	s1.strvalid();
	s1.stringout();
	getch();
}