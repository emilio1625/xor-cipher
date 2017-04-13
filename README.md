# xor-cipher
Small and simple xor cipher

In cryptography, the simple XOR cipher is a type of additive cipher, an
encryption algorithm that operates according to the principles:
 *  A ⊕ 0 = A,
 *  A ⊕ A = 0,
 *  (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C),
 *  (B ⊕ A) ⊕ A = B ⊕ 0 = B,
where ⊕ denotes the exclusive disjunction (XOR) operation.[¹](https://en.wikipedia.org/wiki/XOR_cipher)

## Quick Usage
* Interactive Mode
  ```shell
  $ ./xor-cipher
  ```
  Xor-cipher will prompt you for the text and key to encrypt/decrypt.
* Encrypt/Decrypt a line of text
  ```shell
  $ ./xor-cipher -t "line to {de,en}crypt" -k "key" [-o "path to file"]
  ```
  Is not recommended to output directly to the shell, use `-o` to specify an
  output file.
* Encrypt/Decrypt a textfile
  ```shell
  $ ./xor-cipher -f "path to file to {de,en}crypt" -k "key" [-o "path to output file"]
  ```
* Encrypt decrypt with a keyfile
  ```shell
  $ ./xor-cipher -f "path to file to {de,en}crypt" -K "keyfile" [-o "path to output file"]
  ```
* More info about usage
  ```shell
  $ ./xor-cipher -h
  ```

## Requiriments
Tested with:
* Python 2.7+, 3.4+
* Linux

For any issue use github issues xD