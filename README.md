# PwnedPwd
Have my passwords been compromised?

[![Latest
Version](https://img.shields.io/pypi/v/pwnedpwd.svg)](https://pypi.python.org/pypi/pwnedpwd)

[![tests](https://github.com/ratoaq2/pwnedpwd/actions/workflows/test.yml/badge.svg)](https://github.com/ratoaq2/pwnedpwd/actions/workflows/test.yml)

[![License](https://img.shields.io/github/license/ratoaq2/pwnedpwd.svg)](https://github.com/ratoaq2/pwnedpwd/blob/master/LICENSE)

  - Project page  
    <https://github.com/ratoaq2/pwnedpwd>

## Info

**PwnedPwd** is a tiny CLI tool which uses the **online** service [Pwned Passwords](https://haveibeenpwned.com/API/v3#PwnedPasswords) to check
whether a given password have been compromised in known data breaches. Credits to [Troy Hunt](https://www.troyhunt.com/) for hosting such service.


## How it works?

Given the input password, this tool will
- hash it using SHA-1 algorithm, resulting in a 40-characters hexadecimal string
- Use the first 5 characters from the generated string to query the online service
- The online service returns a list of all matching hashes for the given prefix
- Verify if your SHA-1 hash is present in the response

For instance, given an input password `P@ssword`
- SHA-1 hash is `9E7C97801CB4CCE87B6C02F98291A6420E6400AD`
- The first 5 characters are `9E7C9`
- We query the online service using `GET https://api.pwnedpasswords.com/range/9E7C9`
- The online service returns a list of all matching hashes (777 hashes for this example):
  ```
  ...
  77B1EE4BF1B49FEB288C7FC65EE604C0C54:24
  780087028CF36AF6A5A1DCF096748FB7090:10
  7801CB4CCE87B6C02F98291A6420E6400AD:10848
  782545129CEA7F3BD1A076F25B94C064CFE:3
  788872DE964354319100FCE0EF4DEA00311:4
  ...
  ```
- We verify that `7801CB4CCE87B6C02F98291A6420E6400AD` is present and have `10848` occurrences in data breaches


## About Pwned Passwords

Extracted from their website:

>> Pwned Passwords are more than half a billion passwords which have previously been exposed in data breaches. The service is detailed in the launch blog post then further expanded on with the release of version 2. The entire data set is both downloadable and searchable online via the Pwned Passwords page.
>> In order to protect the value of the source password being searched for, Pwned Passwords also implements a k-Anonymity model that allows a password to be searched for by partial hash.

Detailed information can be found
- https://haveibeenpwned.com/API/v3#PwnedPasswords
- https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/

## Installation

```bash
$ [sudo] pip install pwnedpwd
```

## Usage

```bash
$ pwnedpwd
Password: ******
[GOOD] Password is not present in any known data breach. (source https://haveibeenpwned.com/Passwords)
```

```bash
$ pwnedpwd
Password: 12345
[BAD] Password appeared 2570791 times in data breaches. (source https://haveibeenpwned.com/Passwords)
```
