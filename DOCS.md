# TE-15 Cryptography Project

## Overview
TE-15 é um projeto de criptografia que fornece funcionalidades para geração de chaves, criptografia e descriptografia de dados. Ele inclui uma interface de linha de comando para facilitar a interação com as funções criptográficas.

## Arquivos
- **te15.py**: Contém as funções principais de criptografia, incluindo geração de chaves, criptografia e descriptografia.
- **example.py**: Demonstra como usar as funções definidas em `te15.py` com exemplos práticos.
- **te15-cli.py**: Implementa uma interface de linha de comando para realizar operações criptográficas.

## Interface de Linha de Comando

### Uso
Para usar a interface de linha de comando, execute o script `te15-cli.py` com as flags apropriadas.

### Flags
- `--keys <diretório>`: Especifica o diretório contendo as chaves.
- `--op <operação>`: Especifica o tipo de operação. Use `encrypt` para criptografar dados ou `decrypt` para descriptografar dados.
- `--mode <modo>`: Especifica o modo de operação. Use `files` para operar em arquivos ou `string` para operar em strings.
- `--toUse <entrada>`: Especifica a string a ser criptografada ou o caminho do arquivo a ser criptografado ou descriptografado.
- `--generate-keys <diretório>`: Gera novas chaves e cria o diretório especificado para armazená-las.
- `--check-keys`: Verifica a validade das chaves no diretório especificado.

### Exemplos
1. **Gerar Chaves**:
   ```bash
   python te15-cli.py --generate-keys ./keys
   ```

2. **Verificar Chaves**:
   ```bash
   python te15-cli.py --check-keys --keys ./keys
   ```

3. **Criptografar uma String**:
   ```bash
   python te15-cli.py --op encrypt --mode string --toUse "Hello, World!" --keys ./keys
   ```

4. **Descriptografar uma String**:
   ```bash
   python te15-cli.py --op decrypt --mode string --toUse "<encrypted_string>" --keys ./keys
   ```

5. **Criptografar um Arquivo**:
   ```bash
   python te15-cli.py --op encrypt --mode files --toUse path/to/input_file.txt --keys ./keys
   ```

6. **Descriptografar um Arquivo**:
   ```bash
   python te15-cli.py --op decrypt --mode files --toUse path/to/input_file.txt.enc --keys ./keys
   ```

## Conclusão
Este projeto fornece uma maneira simples e eficaz de lidar com operações criptográficas por meio de uma interface de linha de comando. Siga os exemplos acima para utilizar as funcionalidades fornecidas pelo projeto TE-15.