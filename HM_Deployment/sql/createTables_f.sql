create table atc_anatomical_gr (
    id serial primary key,
    name varchar(200) not null,
    atc_code varchar(1) not null
);

create table atc_therapeutic_subgr (
    id serial primary key,
    atc_anatomical_gr_id int references atc_anatomical_gr(id),
    name varchar(200) not null,
    atc_code varchar(3) not null
);

create table atc_pharmacological_subgr (
    id serial primary key,
    atc_therapeutic_subgr_id int references atc_therapeutic_subgr(id),
    name varchar(200) not null,
    atc_code varchar(4) not null
);

create table atc_chemical_subgr (
    id serial primary key,
    atc_pharmacological_subgr_id int references atc_pharmacological_subgr(id),
    name varchar(200) not null,
    atc_code varchar(5) not null
);

create table atc_chemical_substance (
    id serial primary key,
    atc_chemical_subgr_id int references atc_chemical_subgr(id),
    name varchar(200) not null,
    atc_code varchar(7) not null
);

create table drugs (
    id serial primary key,
    name varchar(200) not null,
    atc_chemical_substance_id int references atc_chemical_substance(id),
    quantity int default 0 not null,
    description varchar(1000) default 'Some description'
);

create table medic_ranks (
    id serial primary key,
    name varchar(200) not null
);

create table suppliers (
    id serial primary key,
    name varchar(200) not null,
    country varchar(50) not null,
    contact_info varchar(200) default 'Some contact info'
);

create table manufacturers (
    id serial primary key,
    name varchar(200) not null,
    country varchar(50) not null,
    contact_info varchar(200) default 'Some contact info'
);

create table drugs_prohibited (
    id serial primary key,
    drug_id int references drugs(id),
    medic_rank_id int references medic_ranks(id)
);

create table drug_supplier (
    id serial primary key,
    drug_id int references drugs(id),
    supplier_id int references suppliers(id)
);

create table drug_manufacturer (
    id serial primary key,
    drug_id int references drugs(id),
    manufacturer_id int references manufacturers(id)
);

create table issued_to_medic (
    id serial primary key,
    medic_fname varchar(50) not null,
    medic_lname varchar(50) not null,
    medic_pname varchar(50) not null,
    medic_rank_id int references medic_ranks(id),
    drug_id int references drugs(id),
    quantity int not null,
    date timestamp not null
);