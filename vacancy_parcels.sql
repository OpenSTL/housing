--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4
-- Dumped by pg_dump version 10.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: vacant_parcels; Type: TABLE; Schema: public; Owner: dacresni
--

CREATE TABLE public.vacant_parcels (
    index bigint,
    "FID" bigint,
    "OBJECTID" bigint,
    "HANDLE" bigint,
    "SITEADDR" text,
    "INSIDE_X" double precision,
    "INSIDE_Y" double precision,
    "Acres" double precision,
    "HandleDbl_x" bigint,
    "FID_1" bigint,
    "OBJECTID_1" bigint,
    "HANDLE_1" bigint,
    "SITEADDR_1" text,
    "Handle_12" bigint,
    "OwnerCat" text,
    "VL_Final" bigint,
    "VB_Final" bigint,
    "VL_A" bigint,
    "VL_B" bigint,
    "VL_C" bigint,
    "VL_D" bigint,
    "VL_E" bigint,
    "VL_F" bigint,
    "VB_A" bigint,
    "VB_B" bigint,
    "VB_C" bigint,
    "VB_D" bigint,
    "VB_E" bigint,
    "VB_F" bigint,
    "VB_G" bigint,
    "VB_H" bigint,
    "BD_VB17" bigint,
    "LU1010" bigint,
    "PrclHasBld" bigint,
    "PrclNoBldg" bigint,
    "For_VB18" bigint,
    "For_VL18" bigint,
    "LRA_VL" bigint,
    "LRA_VB" bigint,
    "LRA_GL" bigint,
    "DP_S2016" bigint,
    "BP_S2016" bigint,
    "OP_S2016" bigint,
    "CondStruc" bigint,
    "CondBU" bigint,
    "TaxBalYear" bigint,
    "YrsTaxDeli" bigint,
    "TaxBal" double precision,
    "ForPropCat" bigint,
    "ForBU_10" bigint,
    "ForBU_2" bigint,
    "ForBU_5" bigint,
    "ForMC_10" bigint,
    "ForMC_2" bigint,
    "ForMC_5" bigint,
    "ForVBRP_10" bigint,
    "ForVBRP_2" bigint,
    "ForVBRP_5" bigint,
    "ForYard_10" bigint,
    "ForYard_2" bigint,
    "ForYard_5" bigint,
    "LRA_AqDate" text,
    "LRA_EnterD" text,
    "LRA_AqYear" bigint,
    "LRA_Tenure" bigint,
    "LRA_Usage" text,
    "LRA_AqType" text,
    "LRA_Status" text,
    "TD3" bigint,
    "TD5" bigint,
    "YrsVacant" bigint,
    "BldgsCom" bigint,
    "ComCat" text,
    "ComType" bigint,
    "ComGrdFlr" bigint,
    "ComStories" text,
    "ComYrBlt" bigint,
    "ComConst" text,
    "ComApts" bigint,
    "BldgsRes" bigint,
    "ResUnits" bigint,
    "ResOccType" text,
    "ResBsmt" text,
    "ResBmFin" text,
    "ResExtWall" text,
    "ResLivArea" bigint,
    "ResStories" text,
    "ResFullBat" bigint,
    "ResHlfBath" bigint,
    "ResAC" bigint,
    "ResACwin" bigint,
    "ResCH" bigint,
    "ResAttic" bigint,
    "ResGarage" bigint,
    "ResYrBlt" bigint,
    "Acres_1" double precision,
    "CityBlock" double precision,
    "Parcel" bigint,
    "OwnerCode" bigint,
    "ParcelID" bigint,
    "LowAddNum" bigint,
    "LowAddSuf" text,
    "HighAddNum" bigint,
    "HighAddSuf" text,
    "StPreDir" text,
    "StName" text,
    "StType" text,
    "StSufDir" text,
    "OwnerName" text,
    "OwnerName2" text,
    "OwnerAddr" text,
    "OwnerCity" text,
    "OwnerState" text,
    "OwnerZIP" bigint,
    "AsrClassCo" bigint,
    "AsrLandUse" bigint,
    "SpecBusDis" bigint,
    "SpecBusD_1" bigint,
    "TIFDist" bigint,
    "AsdLand" text,
    "AsdImprove" text,
    "AsdTotal" text,
    "BillLand" text,
    "BillImprov" text,
    "BillTotal" text,
    "AprLand" text,
    "CostAprImp" text,
    "CDALandUse" bigint,
    "Zoning" text,
    "ResSalePri" bigint,
    "ResSaleDat" text,
    "VacBldgYea" bigint,
    "GeoCityBlo" double precision,
    "Ward10" bigint,
    "Precinct10" bigint,
    "Nbrhd_x" bigint,
    "CDADist" bigint,
    "CDASubDist" bigint,
    "PoliceDist" bigint,
    "CensTract1" bigint,
    "CensBlock1" bigint,
    "HouseConsD" bigint,
    "ZIP" bigint,
    "OnFloodBlo" bigint,
    "GisCityBLo" double precision,
    "GisParcel" bigint,
    "GisOwnerCo" bigint,
    "Parcel9" bigint,
    "VB_DemoCk" bigint,
    "NOTvacant" bigint,
    "YardChg5_2" bigint,
    "Handle__13" bigint,
    "Owner" text,
    "VL_G" bigint,
    "VacCatTxt" text,
    "AsdTtl2" bigint,
    "Frontage_x" double precision,
    "HandleDbl_y" bigint,
    "Frontage_y" double precision,
    "Nbrhd_y" bigint,
    "AsrNbrhd" bigint,
    "Neigh #" double precision,
    "Neighborhood Name" text,
    "Assessors Neigh" double precision,
    "Vacant Land Sq. Ft. Price" double precision,
    "Vacant Vandalized Residential Buildings per Unit" double precision,
    "Residential New Construction" double precision,
    "Side Lots" double precision,
    frontage double precision,
    "SqFt" double precision,
    bldg_price double precision,
    vacant_price double precision,
    side_lot_price double precision
);


ALTER TABLE public.vacant_parcels OWNER TO dacresni;

--
-- Name: ix_vacant_parcels_index; Type: INDEX; Schema: public; Owner: dacresni
--

CREATE INDEX ix_vacant_parcels_index ON public.vacant_parcels USING btree (index);


--
-- PostgreSQL database dump complete
--

