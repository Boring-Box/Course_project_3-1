CREATE ROLE "pharmacy_privileged_users" NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
CREATE ROLE "pharmacy_standard_users" NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

CREATE USER pharmacy_admin WITH PASSWORD 'admin';
CREATE USER pharmacy_worker WITH PASSWORD 'standard';

GRANT "pharmacy_privileged_users" TO pharmacy_admin;
GRANT "pharmacy_standard_users" TO pharmacy_worker;

GRANT CONNECT ON DATABASE pharmacy_db TO pharmacy_admin;
GRANT CONNECT ON DATABASE pharmacy_db TO pharmacy_worker;

\c pharmacy_db

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public 
TO GROUP "pharmacy_privileged_users";

GRANT SELECT 
ON TABLE atc_anatomical_gr, atc_therapeutic_subgr, atc_pharmacological_subgr, 
atc_chemical_subgr, atc_chemical_substance, issued_to_medic, medic_ranks 
TO GROUP "pharmacy_standard_users";

GRANT SELECT, INSERT, UPDATE 
ON TABLE drugs, suppliers, manufacturers, drug_supplier, drug_manufacturer 
TO GROUP "pharmacy_standard_users";

GRANT SELECT, INSERT, DELETE 
ON TABLE drugs_prohibited 
TO GROUP "pharmacy_standard_users";

GRANT SELECT, USAGE 
ON TABLE drugs_id_seq, suppliers_id_seq, manufacturers_id_seq, 
drug_supplier_id_seq, drug_manufacturer_id_seq 
TO GROUP "pharmacy_standard_users";

GRANT SELECT, USAGE 
ON TABLE atc_anatomical_gr_id_seq, atc_therapeutic_subgr_id_seq, 
atc_pharmacological_subgr_id_seq, atc_chemical_subgr_id_seq, 
atc_chemical_substance_id_seq, issued_to_medic_id_seq, medic_ranks_id_seq 
TO GROUP "pharmacy_standard_users";

GRANT SELECT, USAGE 
ON TABLE drugs_prohibited_id_seq 
TO GROUP "pharmacy_standard_users";