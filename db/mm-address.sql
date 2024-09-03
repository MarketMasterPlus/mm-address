-- mm-address/db/mm-address.sql

-- Create the marketmaster database
CREATE DATABASE marketmaster;

\connect marketmaster;

-- Create a table for addresses
CREATE TABLE IF NOT EXISTS address (
    id SERIAL PRIMARY KEY,
    street VARCHAR(128) NOT NULL,
    number VARCHAR(10),
    city VARCHAR(64) NOT NULL,
    state VARCHAR(64) NOT NULL,
    cep VARCHAR(20) NOT NULL,
    neighborhood VARCHAR(100),
    complement VARCHAR(128)
);

-- Optionally, add indexes for commonly queried columns
CREATE INDEX IF NOT EXISTS idx_addresses_cep ON address(cep);
CREATE INDEX IF NOT EXISTS idx_addresses_city ON address(city);
CREATE INDEX IF NOT EXISTS idx_addresses_state ON address(state);
