#1- soma, 2-subtração, 3- multiplicação. 4- divisão, 0- sair

resultado = ''
loop do
    puts resultado
    puts 'Selecione uma opção:'
    puts '1- Somar'
    puts '2- Subtrair'
    puts '3- Multiplicar'
    puts '4- Dividir'
    puts '0- Sair'

    opcao = gets.chomp.to_i

    case opcao
    when 1
        num1 = gets.chomp.to_f
        num2 = gets.chomp.to_f
        resultado = "A soma de #{num1} e #{num2} é: #{num1 + num2}"
    when 2
        num1 = gets.chomp.to_f
        num2 = gets.chomp.to_f
        if num1 < num2
            puts "#{num2} - #{num1} é maior"
            num1, num2 = num2, num1
        end
        resultado = "A subtração de #{num1} por #{num2} é: #{num1 - num2}"
    when 3
        num1 = gets.chomp.to_f
        num2 = gets.chomp.to_f
        resultado = "A multiplicação de #{num1} por #{num2} é: #{num1 * num2}"
    when 4
        num1 = gets.chomp.to_f
        num2 = gets.chomp.to_f
        if num2 == 0
            puts "Não pode dividir por zero!"
        else
            resultado = "A divisão de #{num1} por #{num2} é: #{num1 / num2}"
        end
    when 0
        break
    end
end