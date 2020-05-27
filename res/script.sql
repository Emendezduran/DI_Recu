-- sqlite pragma
PRAGMA foreign_keys=1;

-- clientes
create table clientes
(
    id        integer     not null
        constraint clientes_pk
            primary key autoincrement,
    nombre    varchar2(12),
    apellido1  varchar2(12),
    apellido2 varchar2(12),
    documento       varchar2(9) not null,
    edad  int,
    provincia varchar2(20)
);

create unique index clientes_dni_uindex
    on clientes (documento);

create unique index clientes_id_uindex
    on clientes (id);


-- productos
create table productos
(
    id          integer not null
        constraint productos_pk
            primary key autoincrement,
    nombre      varchar2(12),
    precio      integer,
    stock       integer,
    categoria_id integer
);

create unique index productos_id_uindex
    on productos (id);


-- categorias
create table categorias
(
     id          integer not null
        constraint categorias_pk
            primary key autoincrement,
    nombre      varchar2(12),
(

create index categorias_id_index
    on categorias (id);


