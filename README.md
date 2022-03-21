## Sobre o Autor
<img   style="border-radius: 50%"  align="left" width="190" height="190" margin-right="150px"  src="https://lh3.googleusercontent.com/pw/AM-JKLUq-TgjEzhoVY_CtieDZgnZNOoIGyAubOEKisc2FKt7HMCSVv4DGHZjixw4Z2_yomTtgUKr0kxFUyUdmOuTyJnQfhgzXEyOVk6JoajO58wYDtWcrDF-EPRjaE1hj2EsZtM-OYgQsDjHGjdny1yGetxeWw=s250-no?authuser=0"> Oi, meu nome é Pedro Savio, faço engenharia de computação no IFPB, sou desenvolvedor Fullstack e esse é o meu linkedin,  [ir para meu linkedin](https://www.linkedin.com/in/pedro-s-04a300129/).

<br/><br/><br/><br/><br/>


# RESTFRAMEWORK COM DJANGO

<img    align="left" width="800"  margin-right="150px"  src="https://soshace.com/wp-content/uploads/2021/01/879-png-3.png">
<br/><br/><br/><br/>
<br/><br/><br/>

#### Criar apis com django


=========UPAR NO GIT NO LINUX

abra o terminal na pasta do seu projeto

    git init
    git add .
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/pedrosavio99/restframework-django.git
    git push -u origin main

    mas vai dar errado pq vc precisa do token de autenticaao kk
    veja esse video bobao

    ( https://www.youtube.com/watch?v=PMP3RmhkzkA )


######### INSTALACAO ======================================

INSTLAR O PIP EO VENV

    apt install python3.8-venv
    sudo pip install virtualenv
    python3 -m venv venv

entrar na venv

    source venv/bin/activate

venv instalada e ativada!
e ja podemos usar o pip

intalar django

    pip install django

instalar o pytcharm

adeeeus visual =/

entrar na pasta bin do pytcharm

    ./pytcharm.sh

criar um projeto:

    django-admin startproject pontos_turisticos .

========================= criar as macros no pytcharm

    em edit configuration (rundebug) crie um arquivopythone dentro dele faça 
    os 3 comandos com nomes iguais ao comandose selecione o menagepy

    -migrate
    -mekemigrations
    -runserver

========================== criar o super user

    python manage.py createsuperuser

    pedrosavio99
    118111

======================== instalando o restfremework

    pip install djangorestframework

    django-admin.py startproject name

    django-admin.py startapp name

    sempre lembre de registrar o restframework no intaled apps


============= Dicas 

    primeiro crie todos os app de sua aplicação faça ate mapas mentais e depois tente realizar as logicas das view e etcs
    resumindo faça os app e seus models e depois tente no admin e so dai faça a logica
	criar e configuar um novo app
	Criar URL > criar serializer > criarviewset


============ Fazer a apificacao ou melhor criar as view/funcoes


============ apos criar os modelos iremos criar as rotas em urllll da pasta raiz  

 
=========== criar o serializer e depois criar o viewset

## Baixar e intalar o postman pois é por ele que testamos nossas apis

<img    align="left" width="800"  margin-right="150px"  src="https://blog.bsource.com.br/assets/img/POSTMAN.png">
<br/><br/><br/><br/>

    MANUAL POSTMAN:

	PONHA NO ESPAÇO PRA URL A ULR LOCAL DE SUA 	API E ESCOLHA O METODO QUE QUERES PASSAR 
	EXEMPLO LOcalhost... e metodo get e lista alguma coisa 

	PUT: vc vai em body, seleciona form-data e digita os campos que quer alterar e enviar sua solicitacao put
	na url vc precisa selecionar o id do que vc quer mudar


	POST: vc faz igual ao put passando todos os parametros necessários e sem o id na url né

	DELETE: ASSIM COMO no put vc seleciona um id na url e deleta e se tentar deletar duas vezes ja vai vir o 404zao 


# recursos avancados (REDEFINIR FUNCOES BASICAS DO REST)

    CRIAR FILTROS 
            perceba que isso é uma logia e como esperado será implmentado em viewset

            esse exemplo sera implementado na api de core

            def get_queryset(self):
                return PontoTuristico.objects.filter(aprovado=True)

            apos criar seu filtro crie também um basename na url da raiz


    SOBRESCREVER OS METODOS GET POST 

        novamente exemplo implemntado na api core view set ok

        GET
            def list(self,request,*args,**kwargs):
                return Response({'modificando o GET': 123}) #isso vaifazer o get rodar essas inhas ao inves do padrão do django
        POST
            def create(self,request,*args,**kwargs):
                return Response({'Modificando o POST': request.data['nome']})
        DELETE
            def destroy(self,request,*args,**kwargs):
            #aqui precisa informar na url o parametros
                return Response({'Modificando o POST': request.data['nome']})
        PUT
            def update(self,request,*args,**kwargs):
            #aqui precisa informar na url o parametros
                return Response({'Modificando o POST': request.data['nome']})
        
        PATCHE

            def partial_update(self,request,*args,**kwargs):
            #aqui precisa informar na url o parametros
                return Response({'Modificando o POST': request.data['nome']})

        ACTION PERSONLAIZADA 

            @action(method=['get'],detail=True)
            def denunciar(self,request,pk=None):

            #DEPENDENDO DA USA ACTION VC PODE PRECISAR INFORMAR NA UL O ID

                return Response({'DENUNCIA PERSONALIZADA': 'isso é um get entao n tem body'})


##  imagens

imagem do ponto PontoTuristico e da atracao

    alteracao do model em PontoTuristico

    foto = models.ImageField(upload_to='pontos_turisticos',null=True,blank=True) #so pra lembrar que esse model ta em core viu n confuda

    em settings na raiz vamos definir o nome da pasta pra salvar as fotos

    MEDIA_ROOT = 'imagens'

    MEDIA_URL = '/media/'

    depois vamos instalar a biblioteca de imgens do python Pillow

    pip install Pillow

    depois adicione no serializer o campo 'foto'

    migrate tudo


    #o bagulho n funciona em ambiente de producao so quando a gente upar na aws 



====================== habilitando filtros em nossa api(como filtrar o query set- dados que sao retornados)

    filtrando por query string
    querystring é quando vc passa informaçõe na url
    exemplo:   localhost:/8000/pontosturisticos/?id=5&nome=acudevelho   #é tudo isso depois da interrogacao
    e passando essas querystrings v consegue realizar uma consulta

    veja um exemplo desses filtros na viewset de core em get_queryset()

    apos implmentar o filtro teste usando um id valido e um nome
    ex: http://127.0.0.1:8000/pontoturistico/?id=4&nome=Parque%20do%20povo%202 #esse nome bugad é pq os espaços são convertidos mas pode passar o nome com espaço




