-- sqlite pragma
PRAGMA foreign_keys=1;

create table categorias
(
    categoria_id     INTEGER not null
        constraint categorias_pk
            primary key autoincrement,
    categoria_nombre varchar
);

create unique index categorias_categoria_id_uindex
    on categorias (categoria_id);

create table clientes
(
    cliente_id         INTEGER not null
        constraint Clientes_pk
            primary key autoincrement,
    cliente_nombre     varchar,
    cliente_apellido_1 varchar,
    cliente_apellido_2 varchar,
    cliente_documento  int,
    cliente_edad       int,
    cliente_provincia  varchar
);

create unique index Clientes_cliente_documento_uindex
    on clientes (cliente_documento);

create unique index Clientes_cliente_id_uindex
    on clientes (cliente_id);

create table productos
(
    producto_id     INTEGER not null,
    producto_nombre varchar,
    producto_precio int,
    producto_stock  int,
    categoria_id    INTEGER
        references categorias
);

create unique index productos_producto_id_uindex
    on productos (producto_id);

insert into categorias
values (null, 'Limpieza'),
       (null, 'Verduras'),
       (null, 'Frutas'),
       (null, 'Higiene'),
       (null, 'Boyeria'),
       (null, 'Bebidas'),
       (null, 'Bebidas Alcoholicas');

insert into productos
values (null, 'multiusos', 3, 20, 1),
       (null, 'patata', 1, 30, 2),
       (null, 'tomate', 1, 100, 3),
       (null, 'desodorante rexona', 3, 200, 4),
       (null, 'donut reyeno', 1, 10, 5),
       (null, 'Pepsi', 2, 250, 6),
       (null, 'Ron Santa Teresa', 12, 50, 7);

insert into clientes
values (null, 'Emilio', 'Perez', 'Gonzalez', '44455566X', 19, 'Pontevedra'),
       (null, 'Francisco', 'Juarez', 'Santana', '44555667B', 21, 'Pontevedra'),
       (null, 'Patricio', 'Mendes', 'Taboada', '44355448F', 33, 'Coruña');


