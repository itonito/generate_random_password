# random password generator

pwgen generates random password strings, but it includes characters that can sometimes be hard to distinguish, such as 0 vs O, and 1 vs l. 

This random password generator intentionally removes character set "10IOloqv" so that the generated passwords are less likely to mis enter. 

# Requirement

It should work on any v3 pythons. It doesn't use non-standard libraries that requires pip install.

# Usage

Simply execute the script with desired password length as the argument.

```bash
% python gen_pass.py 16
length: 16
password: M3nNiK9TbgChZFbe
```

