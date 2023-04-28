from main import app, database

#with app.app_context():
    #database.create_all()

'''with app.app_context():
    usuario = Usuario(username='Juliana', email='julianaaigueira@gmail.com', senha='123456')

    database.session.add(usuario)

    database.session.commit()'''


'''with app.app_context():
    meus_usuarios = Usuario.query.all()
    print(meus_usuarios)
    primeiro_usuario = Usuario.query.first()
    print(primeiro_usuario)
    print(primeiro_usuario.email)
    print(primeiro_usuario.posts)'''

'''with app.app_context():
    usuario_teste = Usuario.query.filter_by(email='julianaaigueira@gmail.com').first()
    print(usuario_teste)
    print(usuario_teste.username)'''

'''with app.app_context():
    meu_post = Post(id_usiario=1, titulo='Primeiro Post da Juliana!', corpo='Aprendendo Flask!')
    database.session.add(meu_post)
    database.session.commit()'''

# with app.app_context():
#     post = Post.query.first()
#     print(post)
#     print(post.titulo)
#     print(post.corpo)
#     print(post.autor.email)


with app.app_context():
    database.create_all()
