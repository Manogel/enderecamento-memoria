
-- Tratamento de condições

With Ada.Text_IO; Use Ada.Text_IO;
With Ada.Integer_Text_IO; Use Ada.Integer_Text_IO;

procedure Condicoes is

x: natural;
nome: string(1..20);
idade: integer;

begin

Put("Meu Software de tratamento de condicoes!!");
New_Line(2);
Put("Infome seu nome: ");
Get_Line(nome, x);
Put("Infome sua idade: ");
Get(idade);
New_Line(2);
Put("Olá ");
Put_Line(nome(1..x));
if idade >= 18 then
Put("Você é maior de idade!!");
else
Put("Você é menor de idade!!");
end if;

end Condicoes;
