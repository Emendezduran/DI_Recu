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
