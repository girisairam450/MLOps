# ShellPractise

## Extract
1. Extracting characters.

The command below shows how to extract the first four characters.

`echo "database" | cut -c1-4`

You should get the string ‘data’ as output.

The command below shows how to extract 5th to 8th characters.

`echo "database" | cut -c5-8`

You should get the string ‘base’ as output.

The command below shows how to extract the 1st and 5th characters.

`echo "database" | cut -c1,5`

You get the output : ‘db’

2. Extracting fields/columns

We can extract a specific column/field from a delimited text file, by mentioning the delimiter using the -d option, or
the field number using the -f option. The /etc/passwd is a “:” delimited file.

The command below extracts user names (the first field) from /etc/passwd.

`cut -d":" -f1 /etc/passwd`

The command below extracts multiple fields 1st, 3rd, and 6th (username, userid, and home directory) from /etc/passwd.

`cut -d":" -f1,3,6 /etc/passwd`

The command below extracts a range of fields 3rd to 6th (userid, groupid, user description and home directory) from /etc/passwd.

`cut -d":" -f3-6 /etc/passwd`


## Translate

1. Translate from one character set to another

The command below translates all lower case alphabets to upper case.
You could also use the pre-defined character sets  for this purpose.

`echo "Shell Scripting" | tr "[a-z]" "[A-Z]"`

`echo "Shell Scripting" | tr  "[A-Z]" "[a-z]"`

or 

`echo "Shell Scripting" | tr "[:lower:]" "[:upper:]"`

`echo "Shell Scripting" | tr "[:upper:]" "[:lower:]"`

2. Squeeze repeating occurrences of characters

The -s option replaces a sequence of repeated characters with a single occurrence of that character.

`ps | tr -s " "`

`ps | tr -s "[:space:]"`


3. Delete characters

We can delete specified characters using the -d  option. The command below deletes all digits.

`echo "My login pin is 5634" | tr -d "[:digit:]"`

The output will be : ‘My login pin is’
