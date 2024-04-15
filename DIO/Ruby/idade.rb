resultado = ''
loop do
puts resultado
puts 'selecione uma opção:'
puts '1- Qual a idade da pessoa?'
puts '0- Sair.'
print   'Digite sua escolha:'

opcao = gets.chomp.to_i

if opcao == 1
    print 'Digite o ano de nascimento: '
    anoNascimento = gets.chomp.to_i
    print 'Digite o ano atual: '
    anoAtual = gets.chomp.to_i
    idade = anoAtual - anoNascimento
    resultado = "Quem nasceu no ano de #{anoNascimento}, tem #{idade} anos em #{anoAtual}"
elsif opcao == 0
    break if opcao == 0
else
    resultado = 'Opção invalida'
end

system = "clear"
end