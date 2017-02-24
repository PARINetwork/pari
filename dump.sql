--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: album_album; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE album_album (
    page_ptr_id integer NOT NULL,
    description text NOT NULL,
    language character varying(7) NOT NULL
);


ALTER TABLE public.album_album OWNER TO pari;

--
-- Name: album_albumslide; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE album_albumslide (
    id integer NOT NULL,
    sort_order integer,
    audio character varying(50) NOT NULL,
    description text NOT NULL,
    created_on timestamp with time zone NOT NULL,
    modified_on timestamp with time zone NOT NULL,
    image_id integer,
    page_id integer NOT NULL
);


ALTER TABLE public.album_albumslide OWNER TO pari;

--
-- Name: album_albumslide_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE album_albumslide_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.album_albumslide_id_seq OWNER TO pari;

--
-- Name: album_albumslide_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE album_albumslide_id_seq OWNED BY album_albumslide.id;


--
-- Name: article_article; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE article_article (
    page_ptr_id integer NOT NULL,
    strap text NOT NULL,
    content text NOT NULL,
    language character varying(7) NOT NULL,
    original_published_date date,
    featured_image_id integer
);


ALTER TABLE public.article_article OWNER TO pari;

--
-- Name: article_article_authors; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE article_article_authors (
    id integer NOT NULL,
    article_id integer NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE public.article_article_authors OWNER TO pari;

--
-- Name: article_article_authors_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE article_article_authors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.article_article_authors_id_seq OWNER TO pari;

--
-- Name: article_article_authors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE article_article_authors_id_seq OWNED BY article_article_authors.id;


--
-- Name: article_article_categories; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE article_article_categories (
    id integer NOT NULL,
    article_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.article_article_categories OWNER TO pari;

--
-- Name: article_article_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE article_article_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.article_article_categories_id_seq OWNER TO pari;

--
-- Name: article_article_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE article_article_categories_id_seq OWNED BY article_article_categories.id;


--
-- Name: article_article_locations; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE article_article_locations (
    id integer NOT NULL,
    article_id integer NOT NULL,
    location_id integer NOT NULL
);


ALTER TABLE public.article_article_locations OWNER TO pari;

--
-- Name: article_article_locations_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE article_article_locations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.article_article_locations_id_seq OWNER TO pari;

--
-- Name: article_article_locations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE article_article_locations_id_seq OWNED BY article_article_locations.id;


--
-- Name: article_article_translators; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE article_article_translators (
    id integer NOT NULL,
    article_id integer NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE public.article_article_translators OWNER TO pari;

--
-- Name: article_article_translators_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE article_article_translators_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.article_article_translators_id_seq OWNER TO pari;

--
-- Name: article_article_translators_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE article_article_translators_id_seq OWNED BY article_article_translators.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO pari;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO pari;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO pari;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO pari;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO pari;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO pari;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO pari;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO pari;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO pari;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO pari;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO pari;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO pari;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: author_author; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE author_author (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(50) NOT NULL,
    email character varying(254),
    twitter_username character varying(50),
    facebook_username character varying(50),
    website character varying(200),
    image_id integer,
    bio text,
    bio_as text,
    bio_bn text,
    bio_en text,
    bio_gu text,
    bio_hi text,
    bio_kn text,
    bio_ml text,
    bio_mr text,
    bio_or text,
    bio_pa text,
    bio_ta text,
    bio_te text,
    bio_ur text,
    bio_lus text
);


ALTER TABLE public.author_author OWNER TO pari;

--
-- Name: author_author_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE author_author_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.author_author_id_seq OWNER TO pari;

--
-- Name: author_author_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE author_author_id_seq OWNED BY author_author.id;


--
-- Name: category_category; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE category_category (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL,
    description text NOT NULL,
    "order" integer NOT NULL,
    image_id integer,
    CONSTRAINT category_category_order_check CHECK (("order" >= 0))
);


ALTER TABLE public.category_category OWNER TO pari;

--
-- Name: category_category_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE category_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_category_id_seq OWNER TO pari;

--
-- Name: category_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE category_category_id_seq OWNED BY category_category.id;


--
-- Name: core_affiximage; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE core_affiximage (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    file character varying(1000) NOT NULL,
    width integer NOT NULL,
    height integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    focal_point_x integer,
    focal_point_y integer,
    focal_point_width integer,
    focal_point_height integer,
    people text NOT NULL,
    event text NOT NULL,
    arrival_date timestamp with time zone,
    published_date timestamp with time zone,
    uploaded_by_user_id integer,
    file_size integer,
    collection_id integer NOT NULL,
    camera character varying(50),
    date timestamp with time zone,
    CONSTRAINT core_affiximage_file_size_check CHECK ((file_size >= 0)),
    CONSTRAINT core_affiximage_focal_point_height_check CHECK ((focal_point_height >= 0)),
    CONSTRAINT core_affiximage_focal_point_width_check CHECK ((focal_point_width >= 0)),
    CONSTRAINT core_affiximage_focal_point_x_check CHECK ((focal_point_x >= 0)),
    CONSTRAINT core_affiximage_focal_point_y_check CHECK ((focal_point_y >= 0))
);


ALTER TABLE public.core_affiximage OWNER TO pari;

--
-- Name: core_affiximage_categories; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE core_affiximage_categories (
    id integer NOT NULL,
    affiximage_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.core_affiximage_categories OWNER TO pari;

--
-- Name: core_affiximage_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE core_affiximage_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_affiximage_categories_id_seq OWNER TO pari;

--
-- Name: core_affiximage_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE core_affiximage_categories_id_seq OWNED BY core_affiximage_categories.id;


--
-- Name: core_affiximage_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE core_affiximage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_affiximage_id_seq OWNER TO pari;

--
-- Name: core_affiximage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE core_affiximage_id_seq OWNED BY core_affiximage.id;


--
-- Name: core_affiximage_locations; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE core_affiximage_locations (
    id integer NOT NULL,
    affiximage_id integer NOT NULL,
    location_id integer NOT NULL
);


ALTER TABLE public.core_affiximage_locations OWNER TO pari;

--
-- Name: core_affiximage_locations_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE core_affiximage_locations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_affiximage_locations_id_seq OWNER TO pari;

--
-- Name: core_affiximage_locations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE core_affiximage_locations_id_seq OWNED BY core_affiximage_locations.id;


--
-- Name: core_affiximage_photographers; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE core_affiximage_photographers (
    id integer NOT NULL,
    affiximage_id integer NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE public.core_affiximage_photographers OWNER TO pari;

--
-- Name: core_affiximage_photographers_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE core_affiximage_photographers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_affiximage_photographers_id_seq OWNER TO pari;

--
-- Name: core_affiximage_photographers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE core_affiximage_photographers_id_seq OWNED BY core_affiximage_photographers.id;


--
-- Name: core_affiximagerendition; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE core_affiximagerendition (
    id integer NOT NULL,
    file character varying(100) NOT NULL,
    width integer NOT NULL,
    height integer NOT NULL,
    focal_point_key character varying(255) NOT NULL,
    filter_id integer NOT NULL,
    image_id integer NOT NULL
);


ALTER TABLE public.core_affiximagerendition OWNER TO pari;

--
-- Name: core_affiximagerendition_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE core_affiximagerendition_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_affiximagerendition_id_seq OWNER TO pari;

--
-- Name: core_affiximagerendition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE core_affiximagerendition_id_seq OWNED BY core_affiximagerendition.id;


--
-- Name: core_contact; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE core_contact (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    email character varying(254) NOT NULL,
    message text NOT NULL,
    created_on timestamp with time zone NOT NULL
);


ALTER TABLE public.core_contact OWNER TO pari;

--
-- Name: core_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE core_contact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.core_contact_id_seq OWNER TO pari;

--
-- Name: core_contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE core_contact_id_seq OWNED BY core_contact.id;


--
-- Name: core_homepage; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE core_homepage (
    page_ptr_id integer NOT NULL,
    announcements text NOT NULL,
    strap text NOT NULL,
    about text NOT NULL,
    language character varying(7) NOT NULL,
    carousel_0_id integer,
    carousel_1_id integer,
    carousel_2_id integer,
    carousel_3_id integer,
    carousel_4_id integer,
    carousel_5_id integer,
    carousel_6_id integer,
    carousel_7_id integer,
    carousel_8_id integer,
    carousel_9_id integer
);


ALTER TABLE public.core_homepage OWNER TO pari;

--
-- Name: core_staticpage; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE core_staticpage (
    page_ptr_id integer NOT NULL,
    content text NOT NULL,
    language character varying(7) NOT NULL
);


ALTER TABLE public.core_staticpage OWNER TO pari;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO pari;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO pari;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO pari;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO pari;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO pari;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO pari;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO pari;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO pari;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO pari;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: face_face; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE face_face (
    page_ptr_id integer NOT NULL,
    description text NOT NULL,
    image_id integer,
    location_id integer,
    language character varying(7) NOT NULL,
    adivasi character varying(50),
    age integer,
    child boolean NOT NULL,
    gender character varying(1),
    occupation character varying(50),
    quote text NOT NULL
);


ALTER TABLE public.face_face OWNER TO pari;

--
-- Name: location_location; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE location_location (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(50) NOT NULL,
    point geometry(Point,4326) NOT NULL,
    block character varying(100),
    district character varying(100) NOT NULL,
    state character varying(50) NOT NULL,
    region character varying(100),
    mandapam character varying(100),
    others character varying(100),
    sub_district character varying(100),
    taluka character varying(100),
    tehsil character varying(100)
);


ALTER TABLE public.location_location OWNER TO pari;

--
-- Name: location_location_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE location_location_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.location_location_id_seq OWNER TO pari;

--
-- Name: location_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE location_location_id_seq OWNED BY location_location.id;


--
-- Name: resources_resource; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE resources_resource (
    page_ptr_id integer NOT NULL,
    date date,
    content text NOT NULL,
    embed_url character varying(200) NOT NULL,
    embed_thumbnail text,
    language character varying(7) NOT NULL
);


ALTER TABLE public.resources_resource OWNER TO pari;

--
-- Name: resources_resource_categories; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE resources_resource_categories (
    id integer NOT NULL,
    resource_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.resources_resource_categories OWNER TO pari;

--
-- Name: resources_resource_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE resources_resource_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resources_resource_categories_id_seq OWNER TO pari;

--
-- Name: resources_resource_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE resources_resource_categories_id_seq OWNED BY resources_resource_categories.id;


--
-- Name: taggit_tag; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE taggit_tag (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL
);


ALTER TABLE public.taggit_tag OWNER TO pari;

--
-- Name: taggit_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE taggit_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.taggit_tag_id_seq OWNER TO pari;

--
-- Name: taggit_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE taggit_tag_id_seq OWNED BY taggit_tag.id;


--
-- Name: taggit_taggeditem; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE taggit_taggeditem (
    id integer NOT NULL,
    object_id integer NOT NULL,
    content_type_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.taggit_taggeditem OWNER TO pari;

--
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE taggit_taggeditem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.taggit_taggeditem_id_seq OWNER TO pari;

--
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE taggit_taggeditem_id_seq OWNED BY taggit_taggeditem.id;


--
-- Name: wagtailcore_collection; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailcore_collection (
    id integer NOT NULL,
    path character varying(255) COLLATE pg_catalog."C" NOT NULL,
    depth integer NOT NULL,
    numchild integer NOT NULL,
    name character varying(255) NOT NULL,
    CONSTRAINT wagtailcore_collection_depth_check CHECK ((depth >= 0)),
    CONSTRAINT wagtailcore_collection_numchild_check CHECK ((numchild >= 0))
);


ALTER TABLE public.wagtailcore_collection OWNER TO pari;

--
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailcore_collection_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailcore_collection_id_seq OWNER TO pari;

--
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailcore_collection_id_seq OWNED BY wagtailcore_collection.id;


--
-- Name: wagtailcore_groupcollectionpermission; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailcore_groupcollectionpermission (
    id integer NOT NULL,
    collection_id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.wagtailcore_groupcollectionpermission OWNER TO pari;

--
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailcore_groupcollectionpermission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailcore_groupcollectionpermission_id_seq OWNER TO pari;

--
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailcore_groupcollectionpermission_id_seq OWNED BY wagtailcore_groupcollectionpermission.id;


--
-- Name: wagtailcore_grouppagepermission; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailcore_grouppagepermission (
    id integer NOT NULL,
    permission_type character varying(20) NOT NULL,
    group_id integer NOT NULL,
    page_id integer NOT NULL
);


ALTER TABLE public.wagtailcore_grouppagepermission OWNER TO pari;

--
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailcore_grouppagepermission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailcore_grouppagepermission_id_seq OWNER TO pari;

--
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailcore_grouppagepermission_id_seq OWNED BY wagtailcore_grouppagepermission.id;


--
-- Name: wagtailcore_page; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailcore_page (
    id integer NOT NULL,
    path character varying(255) COLLATE pg_catalog."C" NOT NULL,
    depth integer NOT NULL,
    numchild integer NOT NULL,
    title character varying(255) NOT NULL,
    slug character varying(255) NOT NULL,
    live boolean NOT NULL,
    has_unpublished_changes boolean NOT NULL,
    url_path text NOT NULL,
    seo_title character varying(255) NOT NULL,
    show_in_menus boolean NOT NULL,
    search_description text NOT NULL,
    go_live_at timestamp with time zone,
    expire_at timestamp with time zone,
    expired boolean NOT NULL,
    content_type_id integer NOT NULL,
    owner_id integer,
    locked boolean NOT NULL,
    latest_revision_created_at timestamp with time zone,
    first_published_at timestamp with time zone,
    CONSTRAINT wagtailcore_page_depth_check CHECK ((depth >= 0)),
    CONSTRAINT wagtailcore_page_numchild_check CHECK ((numchild >= 0))
);


ALTER TABLE public.wagtailcore_page OWNER TO pari;

--
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailcore_page_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailcore_page_id_seq OWNER TO pari;

--
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailcore_page_id_seq OWNED BY wagtailcore_page.id;


--
-- Name: wagtailcore_pagerevision; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailcore_pagerevision (
    id integer NOT NULL,
    submitted_for_moderation boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    content_json text NOT NULL,
    approved_go_live_at timestamp with time zone,
    page_id integer NOT NULL,
    user_id integer
);


ALTER TABLE public.wagtailcore_pagerevision OWNER TO pari;

--
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailcore_pagerevision_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailcore_pagerevision_id_seq OWNER TO pari;

--
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailcore_pagerevision_id_seq OWNED BY wagtailcore_pagerevision.id;


--
-- Name: wagtailcore_pageviewrestriction; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailcore_pageviewrestriction (
    id integer NOT NULL,
    password character varying(255) NOT NULL,
    page_id integer NOT NULL
);


ALTER TABLE public.wagtailcore_pageviewrestriction OWNER TO pari;

--
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailcore_pageviewrestriction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailcore_pageviewrestriction_id_seq OWNER TO pari;

--
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailcore_pageviewrestriction_id_seq OWNED BY wagtailcore_pageviewrestriction.id;


--
-- Name: wagtailcore_site; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailcore_site (
    id integer NOT NULL,
    hostname character varying(255) NOT NULL,
    port integer NOT NULL,
    is_default_site boolean NOT NULL,
    root_page_id integer NOT NULL,
    site_name character varying(255)
);


ALTER TABLE public.wagtailcore_site OWNER TO pari;

--
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailcore_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailcore_site_id_seq OWNER TO pari;

--
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailcore_site_id_seq OWNED BY wagtailcore_site.id;


--
-- Name: wagtaildocs_document; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtaildocs_document (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    file character varying(100) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    uploaded_by_user_id integer,
    collection_id integer NOT NULL
);


ALTER TABLE public.wagtaildocs_document OWNER TO pari;

--
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtaildocs_document_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtaildocs_document_id_seq OWNER TO pari;

--
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtaildocs_document_id_seq OWNED BY wagtaildocs_document.id;


--
-- Name: wagtailembeds_embed; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailembeds_embed (
    id integer NOT NULL,
    url character varying(200) NOT NULL,
    max_width smallint,
    type character varying(10) NOT NULL,
    html text NOT NULL,
    title text NOT NULL,
    author_name text NOT NULL,
    provider_name text NOT NULL,
    thumbnail_url character varying(200),
    width integer,
    height integer,
    last_updated timestamp with time zone NOT NULL
);


ALTER TABLE public.wagtailembeds_embed OWNER TO pari;

--
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailembeds_embed_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailembeds_embed_id_seq OWNER TO pari;

--
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailembeds_embed_id_seq OWNED BY wagtailembeds_embed.id;


--
-- Name: wagtailforms_formsubmission; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailforms_formsubmission (
    id integer NOT NULL,
    form_data text NOT NULL,
    submit_time timestamp with time zone NOT NULL,
    page_id integer NOT NULL
);


ALTER TABLE public.wagtailforms_formsubmission OWNER TO pari;

--
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailforms_formsubmission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailforms_formsubmission_id_seq OWNER TO pari;

--
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailforms_formsubmission_id_seq OWNED BY wagtailforms_formsubmission.id;


--
-- Name: wagtailimages_filter; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailimages_filter (
    id integer NOT NULL,
    spec character varying(255) NOT NULL
);


ALTER TABLE public.wagtailimages_filter OWNER TO pari;

--
-- Name: wagtailimages_filter_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailimages_filter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailimages_filter_id_seq OWNER TO pari;

--
-- Name: wagtailimages_filter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailimages_filter_id_seq OWNED BY wagtailimages_filter.id;


--
-- Name: wagtailimages_image; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailimages_image (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    file character varying(100) NOT NULL,
    width integer NOT NULL,
    height integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    focal_point_x integer,
    focal_point_y integer,
    focal_point_width integer,
    focal_point_height integer,
    uploaded_by_user_id integer,
    file_size integer,
    collection_id integer NOT NULL,
    CONSTRAINT wagtailimages_image_file_size_check CHECK ((file_size >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_height_check CHECK ((focal_point_height >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_width_check CHECK ((focal_point_width >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_x_check CHECK ((focal_point_x >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_y_check CHECK ((focal_point_y >= 0))
);


ALTER TABLE public.wagtailimages_image OWNER TO pari;

--
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailimages_image_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailimages_image_id_seq OWNER TO pari;

--
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailimages_image_id_seq OWNED BY wagtailimages_image.id;


--
-- Name: wagtailimages_rendition; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailimages_rendition (
    id integer NOT NULL,
    file character varying(100) NOT NULL,
    width integer NOT NULL,
    height integer NOT NULL,
    focal_point_key character varying(255) NOT NULL,
    filter_id integer NOT NULL,
    image_id integer NOT NULL
);


ALTER TABLE public.wagtailimages_rendition OWNER TO pari;

--
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailimages_rendition_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailimages_rendition_id_seq OWNER TO pari;

--
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailimages_rendition_id_seq OWNED BY wagtailimages_rendition.id;


--
-- Name: wagtailredirects_redirect; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailredirects_redirect (
    id integer NOT NULL,
    old_path character varying(255) NOT NULL,
    is_permanent boolean NOT NULL,
    redirect_link character varying(200) NOT NULL,
    redirect_page_id integer,
    site_id integer
);


ALTER TABLE public.wagtailredirects_redirect OWNER TO pari;

--
-- Name: wagtailredirects_redirect_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailredirects_redirect_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailredirects_redirect_id_seq OWNER TO pari;

--
-- Name: wagtailredirects_redirect_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailredirects_redirect_id_seq OWNED BY wagtailredirects_redirect.id;


--
-- Name: wagtailsearch_editorspick; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailsearch_editorspick (
    id integer NOT NULL,
    sort_order integer,
    description text NOT NULL,
    page_id integer NOT NULL,
    query_id integer NOT NULL
);


ALTER TABLE public.wagtailsearch_editorspick OWNER TO pari;

--
-- Name: wagtailsearch_editorspick_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailsearch_editorspick_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailsearch_editorspick_id_seq OWNER TO pari;

--
-- Name: wagtailsearch_editorspick_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailsearch_editorspick_id_seq OWNED BY wagtailsearch_editorspick.id;


--
-- Name: wagtailsearch_query; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailsearch_query (
    id integer NOT NULL,
    query_string character varying(255) NOT NULL
);


ALTER TABLE public.wagtailsearch_query OWNER TO pari;

--
-- Name: wagtailsearch_query_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailsearch_query_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailsearch_query_id_seq OWNER TO pari;

--
-- Name: wagtailsearch_query_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailsearch_query_id_seq OWNED BY wagtailsearch_query.id;


--
-- Name: wagtailsearch_querydailyhits; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailsearch_querydailyhits (
    id integer NOT NULL,
    date date NOT NULL,
    hits integer NOT NULL,
    query_id integer NOT NULL
);


ALTER TABLE public.wagtailsearch_querydailyhits OWNER TO pari;

--
-- Name: wagtailsearch_querydailyhits_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailsearch_querydailyhits_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailsearch_querydailyhits_id_seq OWNER TO pari;

--
-- Name: wagtailsearch_querydailyhits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailsearch_querydailyhits_id_seq OWNED BY wagtailsearch_querydailyhits.id;


--
-- Name: wagtailusers_userprofile; Type: TABLE; Schema: public; Owner: pari; Tablespace: 
--

CREATE TABLE wagtailusers_userprofile (
    id integer NOT NULL,
    submitted_notifications boolean NOT NULL,
    approved_notifications boolean NOT NULL,
    rejected_notifications boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.wagtailusers_userprofile OWNER TO pari;

--
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: pari
--

CREATE SEQUENCE wagtailusers_userprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wagtailusers_userprofile_id_seq OWNER TO pari;

--
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pari
--

ALTER SEQUENCE wagtailusers_userprofile_id_seq OWNED BY wagtailusers_userprofile.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY album_albumslide ALTER COLUMN id SET DEFAULT nextval('album_albumslide_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_authors ALTER COLUMN id SET DEFAULT nextval('article_article_authors_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_categories ALTER COLUMN id SET DEFAULT nextval('article_article_categories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_locations ALTER COLUMN id SET DEFAULT nextval('article_article_locations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_translators ALTER COLUMN id SET DEFAULT nextval('article_article_translators_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY author_author ALTER COLUMN id SET DEFAULT nextval('author_author_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY category_category ALTER COLUMN id SET DEFAULT nextval('category_category_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage ALTER COLUMN id SET DEFAULT nextval('core_affiximage_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage_categories ALTER COLUMN id SET DEFAULT nextval('core_affiximage_categories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage_locations ALTER COLUMN id SET DEFAULT nextval('core_affiximage_locations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage_photographers ALTER COLUMN id SET DEFAULT nextval('core_affiximage_photographers_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximagerendition ALTER COLUMN id SET DEFAULT nextval('core_affiximagerendition_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_contact ALTER COLUMN id SET DEFAULT nextval('core_contact_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY location_location ALTER COLUMN id SET DEFAULT nextval('location_location_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY resources_resource_categories ALTER COLUMN id SET DEFAULT nextval('resources_resource_categories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY taggit_tag ALTER COLUMN id SET DEFAULT nextval('taggit_tag_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY taggit_taggeditem ALTER COLUMN id SET DEFAULT nextval('taggit_taggeditem_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_collection ALTER COLUMN id SET DEFAULT nextval('wagtailcore_collection_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_groupcollectionpermission ALTER COLUMN id SET DEFAULT nextval('wagtailcore_groupcollectionpermission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_grouppagepermission ALTER COLUMN id SET DEFAULT nextval('wagtailcore_grouppagepermission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_page ALTER COLUMN id SET DEFAULT nextval('wagtailcore_page_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_pagerevision ALTER COLUMN id SET DEFAULT nextval('wagtailcore_pagerevision_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_pageviewrestriction ALTER COLUMN id SET DEFAULT nextval('wagtailcore_pageviewrestriction_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_site ALTER COLUMN id SET DEFAULT nextval('wagtailcore_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtaildocs_document ALTER COLUMN id SET DEFAULT nextval('wagtaildocs_document_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailembeds_embed ALTER COLUMN id SET DEFAULT nextval('wagtailembeds_embed_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailforms_formsubmission ALTER COLUMN id SET DEFAULT nextval('wagtailforms_formsubmission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailimages_filter ALTER COLUMN id SET DEFAULT nextval('wagtailimages_filter_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailimages_image ALTER COLUMN id SET DEFAULT nextval('wagtailimages_image_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailimages_rendition ALTER COLUMN id SET DEFAULT nextval('wagtailimages_rendition_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailredirects_redirect ALTER COLUMN id SET DEFAULT nextval('wagtailredirects_redirect_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailsearch_editorspick ALTER COLUMN id SET DEFAULT nextval('wagtailsearch_editorspick_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailsearch_query ALTER COLUMN id SET DEFAULT nextval('wagtailsearch_query_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailsearch_querydailyhits ALTER COLUMN id SET DEFAULT nextval('wagtailsearch_querydailyhits_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailusers_userprofile ALTER COLUMN id SET DEFAULT nextval('wagtailusers_userprofile_id_seq'::regclass);


--
-- Data for Name: album_album; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY album_album (page_ptr_id, description, language) FROM stdin;
5	<p>The story of Murugaiya and his family of weavers</p>	en
\.


--
-- Data for Name: album_albumslide; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY album_albumslide (id, sort_order, audio, description, created_on, modified_on, image_id, page_id) FROM stdin;
\.


--
-- Name: album_albumslide_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('album_albumslide_id_seq', 1, true);


--
-- Data for Name: article_article; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY article_article (page_ptr_id, strap, content, language, original_published_date, featured_image_id) FROM stdin;
\.


--
-- Data for Name: article_article_authors; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY article_article_authors (id, article_id, author_id) FROM stdin;
\.


--
-- Name: article_article_authors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('article_article_authors_id_seq', 1, false);


--
-- Data for Name: article_article_categories; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY article_article_categories (id, article_id, category_id) FROM stdin;
\.


--
-- Name: article_article_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('article_article_categories_id_seq', 1, false);


--
-- Data for Name: article_article_locations; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY article_article_locations (id, article_id, location_id) FROM stdin;
\.


--
-- Name: article_article_locations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('article_article_locations_id_seq', 1, false);


--
-- Data for Name: article_article_translators; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY article_article_translators (id, article_id, author_id) FROM stdin;
\.


--
-- Name: article_article_translators_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('article_article_translators_id_seq', 1, false);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY auth_group (id, name) FROM stdin;
1	Moderators
2	Editors
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('auth_group_id_seq', 2, true);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	2	1
5	2	2
6	2	3
7	1	4
8	2	4
9	1	5
10	1	6
11	1	7
12	2	5
13	2	6
14	2	7
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 14, true);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add image	2	add_image
2	Can change image	2	change_image
3	Can delete image	2	delete_image
4	Can access Wagtail admin	3	access_admin
5	Can add document	4	add_document
6	Can change document	4	change_document
7	Can delete document	4	delete_document
8	Can add log entry	5	add_logentry
9	Can change log entry	5	change_logentry
10	Can delete log entry	5	delete_logentry
11	Can add permission	6	add_permission
12	Can change permission	6	change_permission
13	Can delete permission	6	delete_permission
14	Can add group	7	add_group
15	Can change group	7	change_group
16	Can delete group	7	delete_group
17	Can add user	8	add_user
18	Can change user	8	change_user
19	Can delete user	8	delete_user
20	Can add content type	9	add_contenttype
21	Can change content type	9	change_contenttype
22	Can delete content type	9	delete_contenttype
23	Can add session	10	add_session
24	Can change session	10	change_session
25	Can delete session	10	delete_session
26	Can add site	11	add_site
27	Can change site	11	change_site
28	Can delete site	11	delete_site
29	Can add Tag	12	add_tag
30	Can change Tag	12	change_tag
31	Can delete Tag	12	delete_tag
32	Can add Tagged Item	13	add_taggeditem
33	Can change Tagged Item	13	change_taggeditem
34	Can delete Tagged Item	13	delete_taggeditem
35	Can add static page	14	add_staticpage
36	Can change static page	14	change_staticpage
37	Can delete static page	14	delete_staticpage
38	Can add home page	15	add_homepage
39	Can change home page	15	change_homepage
40	Can delete home page	15	delete_homepage
41	Can add affix image	16	add_affiximage
42	Can change affix image	16	change_affiximage
43	Can delete affix image	16	delete_affiximage
44	Can add affix image rendition	17	add_affiximagerendition
45	Can change affix image rendition	17	change_affiximagerendition
46	Can delete affix image rendition	17	delete_affiximagerendition
47	Can add contact	18	add_contact
48	Can change contact	18	change_contact
49	Can delete contact	18	delete_contact
50	Can add location	19	add_location
51	Can change location	19	change_location
52	Can delete location	19	delete_location
53	Can add author	20	add_author
54	Can change author	20	change_author
55	Can delete author	20	delete_author
56	Can add category	21	add_category
57	Can change category	21	change_category
58	Can delete category	21	delete_category
59	Can add article	22	add_article
60	Can change article	22	change_article
61	Can delete article	22	delete_article
62	Can add album	23	add_album
63	Can change album	23	change_album
64	Can delete album	23	delete_album
65	Can add album slide	24	add_albumslide
66	Can change album slide	24	change_albumslide
67	Can delete album slide	24	delete_albumslide
68	Can add face	25	add_face
69	Can change face	25	change_face
70	Can delete face	25	delete_face
71	Can add resource	26	add_resource
72	Can change resource	26	change_resource
73	Can delete resource	26	delete_resource
74	Can add site	27	add_site
75	Can change site	27	change_site
76	Can delete site	27	delete_site
77	Can add page	1	add_page
78	Can change page	1	change_page
79	Can delete page	1	delete_page
80	Can add page revision	28	add_pagerevision
81	Can change page revision	28	change_pagerevision
82	Can delete page revision	28	delete_pagerevision
83	Can add group page permission	29	add_grouppagepermission
84	Can change group page permission	29	change_grouppagepermission
85	Can delete group page permission	29	delete_grouppagepermission
86	Can add page view restriction	30	add_pageviewrestriction
87	Can change page view restriction	30	change_pageviewrestriction
88	Can delete page view restriction	30	delete_pageviewrestriction
89	Can add collection	31	add_collection
90	Can change collection	31	change_collection
91	Can delete collection	31	delete_collection
92	Can add group collection permission	32	add_groupcollectionpermission
93	Can change group collection permission	32	change_groupcollectionpermission
94	Can delete group collection permission	32	delete_groupcollectionpermission
95	Can add user profile	33	add_userprofile
96	Can change user profile	33	change_userprofile
97	Can delete user profile	33	delete_userprofile
98	Can add filter	34	add_filter
99	Can change filter	34	change_filter
100	Can delete filter	34	delete_filter
101	Can add rendition	35	add_rendition
102	Can change rendition	35	change_rendition
103	Can delete rendition	35	delete_rendition
104	Can add embed	36	add_embed
105	Can change embed	36	change_embed
106	Can delete embed	36	delete_embed
107	Can add query	37	add_query
108	Can change query	37	change_query
109	Can delete query	37	delete_query
110	Can add Query Daily Hits	38	add_querydailyhits
111	Can change Query Daily Hits	38	change_querydailyhits
112	Can delete Query Daily Hits	38	delete_querydailyhits
113	Can add redirect	39	add_redirect
114	Can change redirect	39	change_redirect
115	Can delete redirect	39	delete_redirect
116	Can add form submission	40	add_formsubmission
117	Can change form submission	40	change_formsubmission
118	Can delete form submission	40	delete_formsubmission
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('auth_permission_id_seq', 118, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$20000$hZ4xWD7MEMux$lNYGIC6yf9R1Y2IVK4BvcWEaPUfU2yQf0fRDBLcI6z8=	2017-02-23 06:21:05.538203+00	t	pari				t	t	2017-02-23 06:21:01.665685+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: author_author; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY author_author (id, name, slug, email, twitter_username, facebook_username, website, image_id, bio, bio_as, bio_bn, bio_en, bio_gu, bio_hi, bio_kn, bio_ml, bio_mr, bio_or, bio_pa, bio_ta, bio_te, bio_ur, bio_lus) FROM stdin;
1	Pari author	pari-author					\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Name: author_author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('author_author_id_seq', 1, true);


--
-- Data for Name: category_category; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY category_category (id, name, slug, description, "order", image_id) FROM stdin;
3	AudioZone	audiozone	Music, conversations, stories	18	1
28	The wild	the-wild	The world of nature	13	1
17	PARI for schools	pari-for-schools	Work done for PARI by students	27	1
19	Faces	faces	The myriad faces of rural India	3	1
22	PhotoZone	photozone	Collection of photographs	19	1
6	One-offs	one-offs	Videos, photos, articles	19	1
14	Healthcare	health	The state of rural health	15	1
18	Things we wear	headgear	Clothing, headgear, jewellery...	19	1
1	The rural in the urban	the-rural-in-the-urban	Migrant workers across India	5	1
12	Women	women	More than half the sky	6	1
16	Getting there	getting-there	Zany rural transportation	12	1
15	Tongues	tongues	The universe of our languages	17	1
10	Things we do	things-we-do	The world of rural labour	0	1
13	Resource conflicts	resource-conflicts	Jal, jungle, zameen	10	1
24	VideoZone	videozone	Videos and multi-media	16	1
8	Farming and its crisis	farming-and-its-crisis	The troubled world of agriculture	2	1
27	Adivasis	adivasis	The first dwellers	7	1
21	Visible Work, Invisible Women	visible-work-invisible-women	Women and work: a photo exhibition	18	1
5	Small world	small-world	A focus on children	11	1
9	Little takes	Little takes	Small, impactful video clips	4	1
2	We are	we-are	Communities and cultures	9	1
4	Foot-soldiers of freedom	foot-soldiers-of-freedom	The last living freedom fighters	10	1
25	Mosaic	folklore	Culture and folklore	16	1
26	Dalits	dalits	Struggles of the oppressed	8	1
7	Things we make	things-we-make	Artisans, artists and craftspersons	1	1
11	Musafir	musafir	Travellers tales, everyday lives	12	1
23	Environment	environment	People, livelihoods, habitats 	16	1
20	Rural sports	sports-games	Games people play	14	1
\.


--
-- Name: category_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('category_category_id_seq', 1, false);


--
-- Data for Name: core_affiximage; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY core_affiximage (id, title, file, width, height, created_at, focal_point_x, focal_point_y, focal_point_width, focal_point_height, people, event, arrival_date, published_date, uploaded_by_user_id, file_size, collection_id, camera, date) FROM stdin;
1	pari.png	original_images/pari.png	620	264	2017-02-23 07:22:29.677976+00	\N	\N	\N	\N			\N	\N	1	36588	1		\N
\.


--
-- Data for Name: core_affiximage_categories; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY core_affiximage_categories (id, affiximage_id, category_id) FROM stdin;
\.


--
-- Name: core_affiximage_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('core_affiximage_categories_id_seq', 1, false);


--
-- Name: core_affiximage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('core_affiximage_id_seq', 1, true);


--
-- Data for Name: core_affiximage_locations; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY core_affiximage_locations (id, affiximage_id, location_id) FROM stdin;
\.


--
-- Name: core_affiximage_locations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('core_affiximage_locations_id_seq', 1, false);


--
-- Data for Name: core_affiximage_photographers; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY core_affiximage_photographers (id, affiximage_id, author_id) FROM stdin;
\.


--
-- Name: core_affiximage_photographers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('core_affiximage_photographers_id_seq', 1, false);


--
-- Data for Name: core_affiximagerendition; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY core_affiximagerendition (id, file, width, height, focal_point_key, filter_id, image_id) FROM stdin;
1	images/pari.max-512x410.png	512	218		1	1
2	images/pari.max-165x165.png	165	70		2	1
3	images/pari.2e16d0ba.fill-512x512.png	264	264	2e16d0ba	3	1
4	images/pari.2e16d0ba.fill-370x300.png	326	264	2e16d0ba	4	1
\.


--
-- Name: core_affiximagerendition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('core_affiximagerendition_id_seq', 4, true);


--
-- Data for Name: core_contact; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY core_contact (id, name, email, message, created_on) FROM stdin;
\.


--
-- Name: core_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('core_contact_id_seq', 1, false);


--
-- Data for Name: core_homepage; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY core_homepage (page_ptr_id, announcements, strap, about, language, carousel_0_id, carousel_1_id, carousel_2_id, carousel_3_id, carousel_4_id, carousel_5_id, carousel_6_id, carousel_7_id, carousel_8_id, carousel_9_id) FROM stdin;
3		[{"type": "tagline_1", "value": "<p>People's Archive of Rural India</p>"}]	[{"type": "column_1", "value": "<p>There is surely much in rural India that should die. Much in rural India that is tyrannical, oppressive, regressive and brutal \\u2014 and which needs to go. Untouchability, feudalism, bonded labour, extreme caste and gender oppression and exploitation, land grab and more.\\u00a0</p>"}]	en	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: core_staticpage; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY core_staticpage (page_ptr_id, content, language) FROM stdin;
7		en
9		en
11		en
13		en
15		en
17		en
19		en
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	wagtailcore	page
2	wagtailimages	image
3	wagtailadmin	admin
4	wagtaildocs	document
5	admin	logentry
6	auth	permission
7	auth	group
8	auth	user
9	contenttypes	contenttype
10	sessions	session
11	sites	site
12	taggit	tag
13	taggit	taggeditem
14	core	staticpage
15	core	homepage
16	core	affiximage
17	core	affiximagerendition
18	core	contact
19	location	location
20	author	author
21	category	category
22	article	article
23	album	album
24	album	albumslide
25	face	face
26	resources	resource
27	wagtailcore	site
28	wagtailcore	pagerevision
29	wagtailcore	grouppagepermission
30	wagtailcore	pageviewrestriction
31	wagtailcore	collection
32	wagtailcore	groupcollectionpermission
33	wagtailusers	userprofile
34	wagtailimages	filter
35	wagtailimages	rendition
36	wagtailembeds	embed
37	wagtailsearch	query
38	wagtailsearch	querydailyhits
39	wagtailredirects	redirect
40	wagtailforms	formsubmission
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('django_content_type_id_seq', 40, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2017-02-23 06:20:01.658915+00
2	auth	0001_initial	2017-02-23 06:20:01.723457+00
3	admin	0001_initial	2017-02-23 06:20:01.747039+00
4	wagtailcore	0001_initial	2017-02-23 06:20:02.014994+00
5	wagtailcore	0002_initial_data	2017-02-23 06:20:02.016387+00
6	wagtailcore	0003_add_uniqueness_constraint_on_group_page_permission	2017-02-23 06:20:02.017486+00
7	wagtailcore	0004_page_locked	2017-02-23 06:20:02.018824+00
8	wagtailcore	0005_add_page_lock_permission_to_moderators	2017-02-23 06:20:02.019967+00
9	wagtailcore	0006_add_lock_page_permission	2017-02-23 06:20:02.021212+00
10	wagtailcore	0007_page_latest_revision_created_at	2017-02-23 06:20:02.022411+00
11	wagtailcore	0008_populate_latest_revision_created_at	2017-02-23 06:20:02.023616+00
12	wagtailcore	0009_remove_auto_now_add_from_pagerevision_created_at	2017-02-23 06:20:02.024799+00
13	wagtailcore	0010_change_page_owner_to_null_on_delete	2017-02-23 06:20:02.025866+00
14	wagtailcore	0011_page_first_published_at	2017-02-23 06:20:02.027136+00
15	wagtailcore	0012_extend_page_slug_field	2017-02-23 06:20:02.028245+00
16	wagtailcore	0013_update_golive_expire_help_text	2017-02-23 06:20:02.029596+00
17	wagtailcore	0014_add_verbose_name	2017-02-23 06:20:02.031564+00
18	wagtailcore	0015_add_more_verbose_names	2017-02-23 06:20:02.032464+00
19	wagtailcore	0016_change_page_url_path_to_text_field	2017-02-23 06:20:02.03373+00
20	wagtailcore	0017_change_edit_page_permission_description	2017-02-23 06:20:02.397014+00
21	wagtailcore	0018_pagerevision_submitted_for_moderation_index	2017-02-23 06:20:02.420343+00
22	wagtailcore	0019_verbose_names_cleanup	2017-02-23 06:20:02.509999+00
23	wagtailcore	0020_add_index_on_page_first_published_at	2017-02-23 06:20:02.532218+00
24	wagtailcore	0021_capitalizeverbose	2017-02-23 06:20:03.155385+00
25	wagtailcore	0022_add_site_name	2017-02-23 06:20:03.177564+00
26	wagtailcore	0023_alter_page_revision_on_delete_behaviour	2017-02-23 06:20:03.209252+00
27	wagtailcore	0024_collection	2017-02-23 06:20:03.221395+00
28	wagtailcore	0025_collection_initial_data	2017-02-23 06:20:03.226569+00
29	wagtailcore	0026_group_collection_permission	2017-02-23 06:20:03.289232+00
30	wagtailcore	0027_fix_collection_path_collation	2017-02-23 06:20:03.297413+00
31	wagtailcore	0024_alter_page_content_type_on_delete_behaviour	2017-02-23 06:20:03.329929+00
32	wagtailcore	0028_merge	2017-02-23 06:20:03.331527+00
33	taggit	0001_initial	2017-02-23 06:20:03.378432+00
34	taggit	0002_auto_20150616_2121	2017-02-23 06:20:03.410384+00
35	wagtailimages	0001_initial	2017-02-23 06:20:03.51635+00
36	wagtailimages	0002_initial_data	2017-02-23 06:20:03.53146+00
37	wagtailimages	0003_fix_focal_point_fields	2017-02-23 06:20:03.642714+00
38	wagtailimages	0004_make_focal_point_key_not_nullable	2017-02-23 06:20:03.681292+00
39	wagtailimages	0005_make_filter_spec_unique	2017-02-23 06:20:03.732706+00
40	wagtailimages	0006_add_verbose_names	2017-02-23 06:20:03.882839+00
41	location	0001_initial	2017-02-23 06:20:03.911865+00
42	category	0001_initial	2017-02-23 06:20:03.92395+00
43	core	0001_initial	2017-02-23 06:20:04.746944+00
44	core	0002_auto_20150730_1040	2017-02-23 06:20:04.796018+00
45	core	0003_auto_20150731_0952	2017-02-23 06:20:05.279386+00
46	core	0004_auto_20160521_1901	2017-02-23 06:20:05.688433+00
47	core	0005_auto_20161129_1950	2017-02-23 06:20:05.778065+00
48	core	0006_auto_20170124_1531	2017-02-23 06:20:05.868366+00
49	author	0001_initial	2017-02-23 06:20:05.925332+00
50	author	0002_author_bio	2017-02-23 06:20:05.976449+00
51	author	0003_auto_20160619_1946	2017-02-23 06:20:06.598667+00
52	author	0004_author_bio_lus	2017-02-23 06:20:06.659142+00
53	author	0005_auto_20170124_1609	2017-02-23 06:20:06.719698+00
54	core	0007_auto_20170217_1247	2017-02-23 06:20:06.793374+00
55	album	0001_initial	2017-02-23 06:20:06.943995+00
56	album	0002_auto_20150731_0952	2017-02-23 06:20:07.018284+00
57	album	0003_auto_20160627_1235	2017-02-23 06:20:07.6337+00
58	album	0004_auto_20161129_1950	2017-02-23 06:20:07.695915+00
59	album	0005_auto_20170124_1531	2017-02-23 06:20:07.749089+00
60	album	0006_auto_20170215_1838	2017-02-23 06:20:07.758737+00
61	album	0007_remove_album_locations	2017-02-23 06:20:07.821738+00
62	album	0008_auto_20170217_1254	2017-02-23 06:20:07.830368+00
63	album	0009_remove_album_photographers	2017-02-23 06:20:07.886236+00
64	category	0002_category_image	2017-02-23 06:20:07.949141+00
65	article	0001_initial	2017-02-23 06:20:08.038749+00
66	article	0002_auto_20150731_0952	2017-02-23 06:20:08.097546+00
67	article	0003_auto_20160619_2025	2017-02-23 06:20:08.227865+00
68	article	0004_auto_20161129_1950	2017-02-23 06:20:08.297795+00
69	article	0005_auto_20170124_1531	2017-02-23 06:20:08.362752+00
70	contenttypes	0002_remove_content_type_name	2017-02-23 06:20:08.548302+00
71	auth	0002_alter_permission_name_max_length	2017-02-23 06:20:08.613549+00
72	auth	0003_alter_user_email_max_length	2017-02-23 06:20:08.684666+00
73	auth	0004_alter_user_username_opts	2017-02-23 06:20:08.76616+00
74	auth	0005_alter_user_last_login_null	2017-02-23 06:20:08.837356+00
75	auth	0006_require_contenttypes_0002	2017-02-23 06:20:08.840033+00
76	core	0008_auto_20170220_1223	2017-02-23 06:20:09.045166+00
77	face	0001_initial	2017-02-23 06:20:09.128267+00
78	face	0002_auto_20161129_1950	2017-02-23 06:20:09.280521+00
79	face	0003_auto_20170124_1531	2017-02-23 06:20:09.366535+00
80	face	0004_auto_20170217_1244	2017-02-23 06:20:10.250267+00
81	location	0002_auto_20170217_1544	2017-02-23 06:20:10.640986+00
82	resources	0001_initial	2017-02-23 06:20:10.728967+00
83	resources	0002_auto_20150731_0952	2017-02-23 06:20:10.809453+00
84	resources	0003_auto_20161129_1950	2017-02-23 06:20:10.888614+00
85	resources	0004_auto_20170124_1531	2017-02-23 06:20:10.972504+00
86	sessions	0001_initial	2017-02-23 06:20:10.987818+00
87	sites	0001_initial	2017-02-23 06:20:11.001266+00
88	wagtailadmin	0001_create_admin_access_permissions	2017-02-23 06:20:11.023184+00
89	wagtaildocs	0001_initial	2017-02-23 06:20:11.107951+00
90	wagtaildocs	0002_initial_data	2017-02-23 06:20:11.12713+00
91	wagtaildocs	0003_add_verbose_names	2017-02-23 06:20:11.383869+00
92	wagtaildocs	0004_capitalizeverbose	2017-02-23 06:20:11.894898+00
93	wagtaildocs	0005_document_collection	2017-02-23 06:20:12.372702+00
94	wagtaildocs	0006_copy_document_permissions_to_collections	2017-02-23 06:20:12.390933+00
95	wagtaildocs	0005_alter_uploaded_by_user_on_delete_action	2017-02-23 06:20:12.49149+00
96	wagtaildocs	0007_merge	2017-02-23 06:20:12.49364+00
97	wagtailembeds	0001_initial	2017-02-23 06:20:12.522405+00
98	wagtailembeds	0002_add_verbose_names	2017-02-23 06:20:12.53292+00
99	wagtailembeds	0003_capitalizeverbose	2017-02-23 06:20:12.542672+00
100	wagtailforms	0001_initial	2017-02-23 06:20:12.621714+00
101	wagtailforms	0002_add_verbose_names	2017-02-23 06:20:12.777792+00
102	wagtailforms	0003_capitalizeverbose	2017-02-23 06:20:12.933391+00
103	wagtailimages	0007_image_file_size	2017-02-23 06:20:13.022095+00
104	wagtailimages	0008_image_created_at_index	2017-02-23 06:20:13.107383+00
105	wagtailimages	0009_capitalizeverbose	2017-02-23 06:20:13.677607+00
106	wagtailimages	0010_change_on_delete_behaviour	2017-02-23 06:20:13.798003+00
107	wagtailimages	0011_image_collection	2017-02-23 06:20:13.892158+00
108	wagtailimages	0012_copy_image_permissions_to_collections	2017-02-23 06:20:13.91285+00
109	wagtailimages	0013_make_rendition_upload_callable	2017-02-23 06:20:14.003282+00
110	wagtailredirects	0001_initial	2017-02-23 06:20:14.099664+00
111	wagtailredirects	0002_add_verbose_names	2017-02-23 06:20:14.307117+00
112	wagtailredirects	0003_make_site_field_editable	2017-02-23 06:20:14.825403+00
113	wagtailredirects	0004_set_unique_on_path_and_site	2017-02-23 06:20:15.021788+00
114	wagtailredirects	0005_capitalizeverbose	2017-02-23 06:20:15.555986+00
115	wagtailsearch	0001_initial	2017-02-23 06:20:15.778893+00
116	wagtailsearch	0002_add_verbose_names	2017-02-23 06:20:16.17712+00
117	wagtailsearch	0003_remove_editors_pick	2017-02-23 06:20:16.284614+00
118	wagtailusers	0001_initial	2017-02-23 06:20:16.380277+00
119	wagtailusers	0002_add_verbose_name_on_userprofile	2017-02-23 06:20:16.664312+00
120	wagtailusers	0003_add_verbose_names	2017-02-23 06:20:16.760918+00
121	wagtailusers	0004_capitalizeverbose	2017-02-23 06:20:17.49948+00
122	wagtailcore	0001_squashed_0016_change_page_url_path_to_text_field	2017-02-23 06:20:17.503741+00
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('django_migrations_id_seq', 122, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
nmh3pkntchce5g8arl3wb7nkb12s74ob	MGQxN2IwMmNlOGQ2ZDNhZTJhZWIyNDEzMDFmZGRlNDVmZmExOThkOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjM0N2VmZTZiMGMyMTYxOTk0ZDM4YTY3MGRmYzIwN2Y3OTkxZWI1ZjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2017-03-09 06:21:05.539958+00
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: face_face; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY face_face (page_ptr_id, description, image_id, location_id, language, adivasi, age, child, gender, occupation, quote) FROM stdin;
\.


--
-- Data for Name: location_location; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY location_location (id, name, slug, point, block, district, state, region, mandapam, others, sub_district, taluka, tehsil) FROM stdin;
\.


--
-- Name: location_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('location_location_id_seq', 1, false);


--
-- Data for Name: resources_resource; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY resources_resource (page_ptr_id, date, content, embed_url, embed_thumbnail, language) FROM stdin;
\.


--
-- Data for Name: resources_resource_categories; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY resources_resource_categories (id, resource_id, category_id) FROM stdin;
\.


--
-- Name: resources_resource_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('resources_resource_categories_id_seq', 1, false);


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY spatial_ref_sys  FROM stdin;
\.


--
-- Data for Name: taggit_tag; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY taggit_tag (id, name, slug) FROM stdin;
\.


--
-- Name: taggit_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('taggit_tag_id_seq', 1, false);


--
-- Data for Name: taggit_taggeditem; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY taggit_taggeditem (id, object_id, content_type_id, tag_id) FROM stdin;
\.


--
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('taggit_taggeditem_id_seq', 1, false);


--
-- Data for Name: wagtailcore_collection; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailcore_collection (id, path, depth, numchild, name) FROM stdin;
1	0001	1	0	Root
\.


--
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailcore_collection_id_seq', 1, true);


--
-- Data for Name: wagtailcore_groupcollectionpermission; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailcore_groupcollectionpermission (id, collection_id, group_id, permission_id) FROM stdin;
1	1	1	5
2	1	2	5
3	1	1	6
4	1	2	6
5	1	1	1
6	1	2	1
7	1	1	2
8	1	2	2
\.


--
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailcore_groupcollectionpermission_id_seq', 8, true);


--
-- Data for Name: wagtailcore_grouppagepermission; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailcore_grouppagepermission (id, permission_type, group_id, page_id) FROM stdin;
1	add	1	1
2	edit	1	1
3	publish	1	1
4	add	2	1
5	edit	2	1
6	lock	1	1
\.


--
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailcore_grouppagepermission_id_seq', 6, true);


--
-- Data for Name: wagtailcore_page; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailcore_page (id, path, depth, numchild, title, slug, live, has_unpublished_changes, url_path, seo_title, show_in_menus, search_description, go_live_at, expire_at, expired, content_type_id, owner_id, locked, latest_revision_created_at, first_published_at) FROM stdin;
1	0001	1	1	Root	root	t	f	/		f		\N	\N	f	1	\N	f	\N	\N
17	000100010008	3	1	acknowledgements	acknowledgements	t	f	/home/acknowledgements/		f		\N	\N	f	14	1	f	2017-02-23 07:04:08.096678+00	2017-02-23 07:04:08.112537+00
4	0001000100010001	4	0	Translations	translations	t	f	/home/home-page/translations/		f		\N	\N	f	1	\N	f	\N	\N
20	0001000100090001	4	0	Translations	translations	t	f	/home/donate/translations/		f		\N	\N	f	1	\N	f	\N	\N
3	000100010001	3	1	Pari	home-page	t	f	/home/home-page/		f		\N	\N	f	15	1	f	2017-02-23 06:24:46.799688+00	2017-02-23 06:22:58.837304+00
6	0001000100020001	4	0	Translations	translations	t	f	/home/the-weavers-of-walahjapet/translations/		f		\N	\N	f	1	\N	f	\N	\N
2	00010001	2	9	Welcome to your new Wagtail site!	home	t	f	/home/		f		\N	\N	f	1	\N	f	\N	\N
19	000100010009	3	1	Donate	donate	t	f	/home/donate/		f		\N	\N	f	14	1	f	2017-02-23 07:04:24.923132+00	2017-02-23 07:04:24.940075+00
5	000100010002	3	1	The weavers of Walahjapet	the-weavers-of-walahjapet	t	f	/home/the-weavers-of-walahjapet/		f		\N	\N	f	23	1	f	2017-02-23 06:27:58.994058+00	2017-02-23 06:27:16.89444+00
8	0001000100030001	4	0	Translations	translations	t	f	/home/contribute/translations/		f		\N	\N	f	1	\N	f	\N	\N
7	000100010003	3	1	Contribute	contribute	t	f	/home/contribute/		f		\N	\N	f	14	1	f	2017-02-23 07:02:02.007458+00	2017-02-23 07:02:02.030945+00
10	0001000100040001	4	0	Translations	translations	t	f	/home/guidelines/translations/		f		\N	\N	f	1	\N	f	\N	\N
9	000100010004	3	1	Guidelines	guidelines	t	f	/home/guidelines/		f		\N	\N	f	14	1	f	2017-02-23 07:02:36.267061+00	2017-02-23 07:02:36.282569+00
12	0001000100050001	4	0	Translations	translations	t	f	/home/about/translations/		f		\N	\N	f	1	\N	f	\N	\N
11	000100010005	3	1	About	about	t	f	/home/about/		f		\N	\N	f	14	1	f	2017-02-23 07:03:04.940802+00	2017-02-23 07:03:04.967425+00
14	0001000100060001	4	0	Translations	translations	t	f	/home/pari-teachers-students/translations/		f		\N	\N	f	1	\N	f	\N	\N
13	000100010006	3	1	pari-teachers-students	pari-teachers-students	t	f	/home/pari-teachers-students/		f		\N	\N	f	14	1	f	2017-02-23 07:03:33.664558+00	2017-02-23 07:03:33.680426+00
16	0001000100070001	4	0	Translations	translations	t	f	/home/about-the-editor/translations/		f		\N	\N	f	1	\N	f	\N	\N
15	000100010007	3	1	about-the-editor	about-the-editor	t	f	/home/about-the-editor/		f		\N	\N	f	14	1	f	2017-02-23 07:03:52.392689+00	2017-02-23 07:03:52.408342+00
18	0001000100080001	4	0	Translations	translations	t	f	/home/acknowledgements/translations/		f		\N	\N	f	1	\N	f	\N	\N
\.


--
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailcore_page_id_seq', 20, true);


--
-- Data for Name: wagtailcore_pagerevision; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailcore_pagerevision (id, submitted_for_moderation, created_at, content_json, approved_go_live_at, page_id, user_id) FROM stdin;
1	f	2017-02-23 06:22:53.62255+00	{"carousel_3": null, "carousel_2": null, "search_description": "", "owner": 1, "latest_revision_created_at": null, "go_live_at": null, "title": "Pari", "carousel_9": null, "seo_title": "", "slug": "pari", "announcements": "", "live": false, "has_unpublished_changes": false, "carousel_8": null, "numchild": 1, "carousel_5": null, "carousel_4": null, "carousel_7": null, "carousel_6": null, "carousel_1": null, "carousel_0": null, "content_type": 15, "show_in_menus": false, "path": "000100010001", "url_path": "/home/pari/", "expired": false, "pk": 3, "about": "[{\\"type\\": \\"column_1\\", \\"value\\": \\"<p>There is surely much in rural India that should die. Much in rural India that is tyrannical, oppressive, regressive and brutal \\\\u2014 and which needs to go. Untouchability, feudalism, bonded labour, extreme caste and gender oppression and exploitation, land grab and more. The tragedy, though, is that the nature of the transformation underway more often tends to bolster the regressive and the barbaric, while undermining the best and the diverse. That too, will be captured here. PARI is both a living journal and an archive. It will generate and host reporting on the countryside that is current and contemporary, while also creating a database of already published stories, reports, videos and audios from as many sources as we can. All PARI\\\\u2019s own content comes under the Creative Commons (<a href=\\\\\\"http://www.ruralindiaonline.org/legal/copyright/\\\\\\">http://www.ruralindiaonline.org/legal/copyright/</a>) and the site is free to access. Also, anyone can contribute to PARI. Write for us, shoot for us, record for us \\\\u2014 your material is welcome so long as it meets the standards of this site and falls within our mandate: the everyday lives of everyday people.</p>\\"}]", "locked": false, "language": "en", "strap": "[{\\"type\\": \\"tagline_1\\", \\"value\\": \\"<p>People's Archive of Rural India</p>\\"}]", "depth": 3, "first_published_at": null, "expire_at": null}	\N	3	1
2	f	2017-02-23 06:22:58.817393+00	{"carousel_3": null, "carousel_2": null, "search_description": "", "owner": 1, "latest_revision_created_at": "2017-02-23T06:22:53.622Z", "go_live_at": null, "title": "Pari", "carousel_9": null, "seo_title": "", "slug": "pari", "announcements": "", "live": false, "has_unpublished_changes": true, "carousel_8": null, "numchild": 1, "carousel_5": null, "carousel_4": null, "carousel_7": null, "carousel_6": null, "carousel_1": null, "carousel_0": null, "content_type": 15, "show_in_menus": false, "path": "000100010001", "url_path": "/home/pari/", "expired": false, "pk": 3, "about": "[{\\"type\\": \\"column_1\\", \\"value\\": \\"<p>There is surely much in rural India that should die. Much in rural India that is tyrannical, oppressive, regressive and brutal \\\\u2014 and which needs to go. Untouchability, feudalism, bonded labour, extreme caste and gender oppression and exploitation, land grab and more. The tragedy, though, is that the nature of the transformation underway more often tends to bolster the regressive and the barbaric, while undermining the best and the diverse. That too, will be captured here. PARI is both a living journal and an archive. It will generate and host reporting on the countryside that is current and contemporary, while also creating a database of already published stories, reports, videos and audios from as many sources as we can. All PARI\\\\u2019s own content comes under the Creative Commons (<a href=\\\\\\"http://www.ruralindiaonline.org/legal/copyright/\\\\\\">http://www.ruralindiaonline.org/legal/copyright/</a>) and the site is free to access. Also, anyone can contribute to PARI. Write for us, shoot for us, record for us \\\\u2014 your material is welcome so long as it meets the standards of this site and falls within our mandate: the everyday lives of everyday people.</p>\\"}]", "locked": false, "language": "en", "strap": "[{\\"type\\": \\"tagline_1\\", \\"value\\": \\"<p>People's Archive of Rural India</p>\\"}]", "depth": 3, "first_published_at": null, "expire_at": null}	\N	3	1
3	f	2017-02-23 06:24:02.178724+00	{"carousel_3": null, "carousel_2": null, "search_description": "", "owner": 1, "latest_revision_created_at": "2017-02-23T06:22:58.817Z", "go_live_at": null, "title": "Pari", "carousel_9": null, "seo_title": "", "slug": "home-page", "announcements": "", "live": true, "has_unpublished_changes": false, "carousel_8": null, "numchild": 1, "carousel_5": null, "carousel_4": null, "carousel_7": null, "carousel_6": null, "carousel_1": null, "carousel_0": null, "content_type": 15, "show_in_menus": false, "path": "000100010001", "url_path": "/home/pari/", "expired": false, "pk": 3, "about": "[{\\"type\\": \\"column_1\\", \\"value\\": \\"<p>There is surely much in rural India that should die. Much in rural India that is tyrannical, oppressive, regressive and brutal \\\\u2014 and which needs to go. Untouchability, feudalism, bonded labour, extreme caste and gender oppression and exploitation, land grab and more. The tragedy, though, is that the nature of the transformation underway more often tends to bolster the regressive and the barbaric, while undermining the best and the diverse. That too, will be captured here. PARI is both a living journal and an archive. It will generate and host reporting on the countryside that is current and contemporary, while also creating a database of already published stories, reports, videos and audios from as many sources as we can. All PARI\\\\u2019s own content comes under the Creative Commons (<a href=\\\\\\"http://www.ruralindiaonline.org/legal/copyright/\\\\\\">http://www.ruralindiaonline.org/legal/copyright/</a>) and the site is free to access. Also, anyone can contribute to PARI. Write for us, shoot for us, record for us \\\\u2014 your material is welcome so long as it meets the standards of this site and falls within our mandate: the everyday lives of everyday people.</p>\\"}]", "locked": false, "language": "en", "strap": "[{\\"type\\": \\"tagline_1\\", \\"value\\": \\"<p>People's Archive of Rural India</p>\\"}]", "depth": 3, "first_published_at": "2017-02-23T06:22:58.837Z", "expire_at": null}	\N	3	1
5	f	2017-02-23 06:27:16.872191+00	{"search_description": "", "owner": 1, "latest_revision_created_at": null, "go_live_at": null, "title": "The weavers of Walahjapet", "seo_title": "", "slug": "the-weavers-of-walahjapet", "live": true, "has_unpublished_changes": false, "description": "<p>The story of Murugaiya and his family of weavers</p>", "numchild": 1, "slides": [{"description": "", "image": null, "created_on": "2017-02-23T06:27:16.862Z", "sort_order": 0, "modified_on": "2017-02-23T06:27:16.862Z", "pk": 1, "audio": "", "page": 5}], "content_type": 23, "show_in_menus": false, "path": "000100010002", "url_path": "/home/the-weavers-of-walahjapet/", "expired": false, "pk": 5, "locked": false, "language": "en", "depth": 3, "first_published_at": null, "expire_at": null}	\N	5	1
6	f	2017-02-23 06:27:58.994058+00	{"search_description": "", "owner": 1, "latest_revision_created_at": "2017-02-23T06:27:16.872Z", "go_live_at": null, "title": "The weavers of Walahjapet", "seo_title": "", "slug": "the-weavers-of-walahjapet", "live": true, "has_unpublished_changes": false, "description": "<p>The story of Murugaiya and his family of weavers</p>", "numchild": 1, "slides": [], "content_type": 23, "show_in_menus": false, "path": "000100010002", "url_path": "/home/the-weavers-of-walahjapet/", "expired": false, "pk": 5, "locked": false, "language": "en", "depth": 3, "first_published_at": "2017-02-23T06:27:16.894Z", "expire_at": null}	\N	5	1
4	f	2017-02-23 06:24:46.799688+00	{"carousel_3": null, "carousel_2": null, "search_description": "", "owner": 1, "latest_revision_created_at": "2017-02-23T06:24:02.178Z", "go_live_at": null, "title": "Pari", "carousel_9": null, "seo_title": "", "slug": "home-page", "announcements": "", "live": true, "has_unpublished_changes": false, "carousel_8": null, "numchild": 1, "carousel_5": null, "carousel_4": null, "carousel_7": null, "carousel_6": null, "carousel_1": null, "carousel_0": null, "content_type": 15, "show_in_menus": false, "path": "000100010001", "url_path": "/home/home-page/", "expired": false, "pk": 3, "about": "[{\\"type\\": \\"column_1\\", \\"value\\": \\"<p>There is surely much in rural India that should die. Much in rural India that is tyrannical, oppressive, regressive and brutal \\\\u2014 and which needs to go. Untouchability, feudalism, bonded labour, extreme caste and gender oppression and exploitation, land grab and more.\\\\u00a0</p>\\"}]", "locked": false, "language": "en", "strap": "[{\\"type\\": \\"tagline_1\\", \\"value\\": \\"<p>People's Archive of Rural India</p>\\"}]", "depth": 3, "first_published_at": "2017-02-23T06:22:58.837Z", "expire_at": null}	\N	3	1
7	f	2017-02-23 07:02:02.007458+00	{"search_description": "", "owner": 1, "latest_revision_created_at": null, "go_live_at": null, "title": "Contribute", "seo_title": "", "slug": "contribute", "content": "", "live": true, "has_unpublished_changes": false, "numchild": 1, "content_type": 14, "show_in_menus": false, "path": "000100010003", "url_path": "/home/contribute/", "expired": false, "pk": 7, "locked": false, "language": "en", "depth": 3, "first_published_at": null, "expire_at": null}	\N	7	1
10	f	2017-02-23 07:03:33.664558+00	{"search_description": "", "owner": 1, "latest_revision_created_at": null, "go_live_at": null, "title": "pari-teachers-students", "seo_title": "", "slug": "pari-teachers-students", "content": "", "live": true, "has_unpublished_changes": false, "numchild": 1, "content_type": 14, "show_in_menus": false, "path": "000100010006", "url_path": "/home/pari-teachers-students/", "expired": false, "pk": 13, "locked": false, "language": "en", "depth": 3, "first_published_at": null, "expire_at": null}	\N	13	1
8	f	2017-02-23 07:02:36.267061+00	{"search_description": "", "owner": 1, "latest_revision_created_at": null, "go_live_at": null, "title": "Guidelines", "seo_title": "", "slug": "guidelines", "content": "", "live": true, "has_unpublished_changes": false, "numchild": 1, "content_type": 14, "show_in_menus": false, "path": "000100010004", "url_path": "/home/guidelines/", "expired": false, "pk": 9, "locked": false, "language": "en", "depth": 3, "first_published_at": null, "expire_at": null}	\N	9	1
9	f	2017-02-23 07:03:04.940802+00	{"search_description": "", "owner": 1, "latest_revision_created_at": null, "go_live_at": null, "title": "About", "seo_title": "", "slug": "about", "content": "", "live": true, "has_unpublished_changes": false, "numchild": 1, "content_type": 14, "show_in_menus": false, "path": "000100010005", "url_path": "/home/about/", "expired": false, "pk": 11, "locked": false, "language": "en", "depth": 3, "first_published_at": null, "expire_at": null}	\N	11	1
13	f	2017-02-23 07:04:24.923132+00	{"search_description": "", "owner": 1, "latest_revision_created_at": null, "go_live_at": null, "title": "Donate", "seo_title": "", "slug": "donate", "content": "", "live": true, "has_unpublished_changes": false, "numchild": 1, "content_type": 14, "show_in_menus": false, "path": "000100010009", "url_path": "/home/donate/", "expired": false, "pk": 19, "locked": false, "language": "en", "depth": 3, "first_published_at": null, "expire_at": null}	\N	19	1
11	f	2017-02-23 07:03:52.392689+00	{"search_description": "", "owner": 1, "latest_revision_created_at": null, "go_live_at": null, "title": "about-the-editor", "seo_title": "", "slug": "about-the-editor", "content": "", "live": true, "has_unpublished_changes": false, "numchild": 1, "content_type": 14, "show_in_menus": false, "path": "000100010007", "url_path": "/home/about-the-editor/", "expired": false, "pk": 15, "locked": false, "language": "en", "depth": 3, "first_published_at": null, "expire_at": null}	\N	15	1
12	f	2017-02-23 07:04:08.096678+00	{"search_description": "", "owner": 1, "latest_revision_created_at": null, "go_live_at": null, "title": "acknowledgements", "seo_title": "", "slug": "acknowledgements", "content": "", "live": true, "has_unpublished_changes": false, "numchild": 1, "content_type": 14, "show_in_menus": false, "path": "000100010008", "url_path": "/home/acknowledgements/", "expired": false, "pk": 17, "locked": false, "language": "en", "depth": 3, "first_published_at": null, "expire_at": null}	\N	17	1
\.


--
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailcore_pagerevision_id_seq', 13, true);


--
-- Data for Name: wagtailcore_pageviewrestriction; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailcore_pageviewrestriction (id, password, page_id) FROM stdin;
\.


--
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailcore_pageviewrestriction_id_seq', 1, false);


--
-- Data for Name: wagtailcore_site; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailcore_site (id, hostname, port, is_default_site, root_page_id, site_name) FROM stdin;
1	localhost	80	t	2	\N
\.


--
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailcore_site_id_seq', 1, true);


--
-- Data for Name: wagtaildocs_document; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtaildocs_document (id, title, file, created_at, uploaded_by_user_id, collection_id) FROM stdin;
\.


--
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtaildocs_document_id_seq', 1, false);


--
-- Data for Name: wagtailembeds_embed; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailembeds_embed (id, url, max_width, type, html, title, author_name, provider_name, thumbnail_url, width, height, last_updated) FROM stdin;
\.


--
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailembeds_embed_id_seq', 1, false);


--
-- Data for Name: wagtailforms_formsubmission; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailforms_formsubmission (id, form_data, submit_time, page_id) FROM stdin;
\.


--
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailforms_formsubmission_id_seq', 1, false);


--
-- Data for Name: wagtailimages_filter; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailimages_filter (id, spec) FROM stdin;
1	max-512x410
2	max-165x165
3	fill-512x512
4	fill-370x300
\.


--
-- Name: wagtailimages_filter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailimages_filter_id_seq', 4, true);


--
-- Data for Name: wagtailimages_image; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailimages_image (id, title, file, width, height, created_at, focal_point_x, focal_point_y, focal_point_width, focal_point_height, uploaded_by_user_id, file_size, collection_id) FROM stdin;
\.


--
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailimages_image_id_seq', 1, false);


--
-- Data for Name: wagtailimages_rendition; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailimages_rendition (id, file, width, height, focal_point_key, filter_id, image_id) FROM stdin;
\.


--
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailimages_rendition_id_seq', 1, false);


--
-- Data for Name: wagtailredirects_redirect; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailredirects_redirect (id, old_path, is_permanent, redirect_link, redirect_page_id, site_id) FROM stdin;
\.


--
-- Name: wagtailredirects_redirect_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailredirects_redirect_id_seq', 1, false);


--
-- Data for Name: wagtailsearch_editorspick; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailsearch_editorspick (id, sort_order, description, page_id, query_id) FROM stdin;
\.


--
-- Name: wagtailsearch_editorspick_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailsearch_editorspick_id_seq', 1, false);


--
-- Data for Name: wagtailsearch_query; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailsearch_query (id, query_string) FROM stdin;
\.


--
-- Name: wagtailsearch_query_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailsearch_query_id_seq', 1, false);


--
-- Data for Name: wagtailsearch_querydailyhits; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailsearch_querydailyhits (id, date, hits, query_id) FROM stdin;
\.


--
-- Name: wagtailsearch_querydailyhits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailsearch_querydailyhits_id_seq', 1, false);


--
-- Data for Name: wagtailusers_userprofile; Type: TABLE DATA; Schema: public; Owner: pari
--

COPY wagtailusers_userprofile (id, submitted_notifications, approved_notifications, rejected_notifications, user_id) FROM stdin;
\.


--
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pari
--

SELECT pg_catalog.setval('wagtailusers_userprofile_id_seq', 1, false);


--
-- Name: album_album_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY album_album
    ADD CONSTRAINT album_album_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: album_albumslide_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY album_albumslide
    ADD CONSTRAINT album_albumslide_pkey PRIMARY KEY (id);


--
-- Name: article_article_authors_article_id_author_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY article_article_authors
    ADD CONSTRAINT article_article_authors_article_id_author_id_key UNIQUE (article_id, author_id);


--
-- Name: article_article_authors_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY article_article_authors
    ADD CONSTRAINT article_article_authors_pkey PRIMARY KEY (id);


--
-- Name: article_article_categories_article_id_category_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY article_article_categories
    ADD CONSTRAINT article_article_categories_article_id_category_id_key UNIQUE (article_id, category_id);


--
-- Name: article_article_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY article_article_categories
    ADD CONSTRAINT article_article_categories_pkey PRIMARY KEY (id);


--
-- Name: article_article_locations_article_id_location_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY article_article_locations
    ADD CONSTRAINT article_article_locations_article_id_location_id_key UNIQUE (article_id, location_id);


--
-- Name: article_article_locations_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY article_article_locations
    ADD CONSTRAINT article_article_locations_pkey PRIMARY KEY (id);


--
-- Name: article_article_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY article_article
    ADD CONSTRAINT article_article_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: article_article_translators_article_id_author_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY article_article_translators
    ADD CONSTRAINT article_article_translators_article_id_author_id_key UNIQUE (article_id, author_id);


--
-- Name: article_article_translators_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY article_article_translators
    ADD CONSTRAINT article_article_translators_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: author_author_name_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY author_author
    ADD CONSTRAINT author_author_name_key UNIQUE (name);


--
-- Name: author_author_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY author_author
    ADD CONSTRAINT author_author_pkey PRIMARY KEY (id);


--
-- Name: category_category_name_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY category_category
    ADD CONSTRAINT category_category_name_key UNIQUE (name);


--
-- Name: category_category_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY category_category
    ADD CONSTRAINT category_category_pkey PRIMARY KEY (id);


--
-- Name: core_affiximage_categories_affiximage_id_category_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_affiximage_categories
    ADD CONSTRAINT core_affiximage_categories_affiximage_id_category_id_key UNIQUE (affiximage_id, category_id);


--
-- Name: core_affiximage_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_affiximage_categories
    ADD CONSTRAINT core_affiximage_categories_pkey PRIMARY KEY (id);


--
-- Name: core_affiximage_locations_affiximage_id_location_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_affiximage_locations
    ADD CONSTRAINT core_affiximage_locations_affiximage_id_location_id_key UNIQUE (affiximage_id, location_id);


--
-- Name: core_affiximage_locations_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_affiximage_locations
    ADD CONSTRAINT core_affiximage_locations_pkey PRIMARY KEY (id);


--
-- Name: core_affiximage_photographers_affiximage_id_author_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_affiximage_photographers
    ADD CONSTRAINT core_affiximage_photographers_affiximage_id_author_id_key UNIQUE (affiximage_id, author_id);


--
-- Name: core_affiximage_photographers_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_affiximage_photographers
    ADD CONSTRAINT core_affiximage_photographers_pkey PRIMARY KEY (id);


--
-- Name: core_affiximage_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_affiximage
    ADD CONSTRAINT core_affiximage_pkey PRIMARY KEY (id);


--
-- Name: core_affiximagerendition_image_id_71515df4882b45cf_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_affiximagerendition
    ADD CONSTRAINT core_affiximagerendition_image_id_71515df4882b45cf_uniq UNIQUE (image_id, filter_id, focal_point_key);


--
-- Name: core_affiximagerendition_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_affiximagerendition
    ADD CONSTRAINT core_affiximagerendition_pkey PRIMARY KEY (id);


--
-- Name: core_contact_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_contact
    ADD CONSTRAINT core_contact_pkey PRIMARY KEY (id);


--
-- Name: core_homepage_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_homepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: core_staticpage_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY core_staticpage
    ADD CONSTRAINT core_staticpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: face_face_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY face_face
    ADD CONSTRAINT face_face_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: location_location_name_1a60b53930dd7938_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY location_location
    ADD CONSTRAINT location_location_name_1a60b53930dd7938_uniq UNIQUE (name, district, state);


--
-- Name: location_location_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY location_location
    ADD CONSTRAINT location_location_pkey PRIMARY KEY (id);


--
-- Name: resources_resource_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY resources_resource_categories
    ADD CONSTRAINT resources_resource_categories_pkey PRIMARY KEY (id);


--
-- Name: resources_resource_categories_resource_id_category_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY resources_resource_categories
    ADD CONSTRAINT resources_resource_categories_resource_id_category_id_key UNIQUE (resource_id, category_id);


--
-- Name: resources_resource_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY resources_resource
    ADD CONSTRAINT resources_resource_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: taggit_tag_name_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY taggit_tag
    ADD CONSTRAINT taggit_tag_name_key UNIQUE (name);


--
-- Name: taggit_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY taggit_tag
    ADD CONSTRAINT taggit_tag_pkey PRIMARY KEY (id);


--
-- Name: taggit_tag_slug_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY taggit_tag
    ADD CONSTRAINT taggit_tag_slug_key UNIQUE (slug);


--
-- Name: taggit_taggeditem_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_collection_path_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_collection
    ADD CONSTRAINT wagtailcore_collection_path_key UNIQUE (path);


--
-- Name: wagtailcore_collection_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_collection
    ADD CONSTRAINT wagtailcore_collection_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_groupcollectionpermi_group_id_7bdcf8bfbcce5581_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcollectionpermi_group_id_7bdcf8bfbcce5581_uniq UNIQUE (group_id, collection_id, permission_id);


--
-- Name: wagtailcore_groupcollectionpermission_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcollectionpermission_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_grouppagepermission_group_id_16e761a1726500_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppagepermission_group_id_16e761a1726500_uniq UNIQUE (group_id, page_id, permission_type);


--
-- Name: wagtailcore_grouppagepermission_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppagepermission_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_page_path_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_path_key UNIQUE (path);


--
-- Name: wagtailcore_page_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_pagerevision_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_pagerevision
    ADD CONSTRAINT wagtailcore_pagerevision_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_pageviewrestriction_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_pageviewrestriction
    ADD CONSTRAINT wagtailcore_pageviewrestriction_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_site_hostname_29d2c7f94ac026_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_hostname_29d2c7f94ac026_uniq UNIQUE (hostname, port);


--
-- Name: wagtailcore_site_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_pkey PRIMARY KEY (id);


--
-- Name: wagtaildocs_document_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_pkey PRIMARY KEY (id);


--
-- Name: wagtailembeds_embed_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailembeds_embed
    ADD CONSTRAINT wagtailembeds_embed_pkey PRIMARY KEY (id);


--
-- Name: wagtailembeds_embed_url_37a13a49926a4846_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailembeds_embed
    ADD CONSTRAINT wagtailembeds_embed_url_37a13a49926a4846_uniq UNIQUE (url, max_width);


--
-- Name: wagtailforms_formsubmission_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailforms_formsubmission
    ADD CONSTRAINT wagtailforms_formsubmission_pkey PRIMARY KEY (id);


--
-- Name: wagtailimages_filter_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailimages_filter
    ADD CONSTRAINT wagtailimages_filter_pkey PRIMARY KEY (id);


--
-- Name: wagtailimages_filter_spec_45e80ac840fed7f8_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailimages_filter
    ADD CONSTRAINT wagtailimages_filter_spec_45e80ac840fed7f8_uniq UNIQUE (spec);


--
-- Name: wagtailimages_image_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_pkey PRIMARY KEY (id);


--
-- Name: wagtailimages_rendition_image_id_742f4fe4119535f1_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendition_image_id_742f4fe4119535f1_uniq UNIQUE (image_id, filter_id, focal_point_key);


--
-- Name: wagtailimages_rendition_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendition_pkey PRIMARY KEY (id);


--
-- Name: wagtailredirects_redirect_old_path_5e354102fcbf9c8b_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_redirect_old_path_5e354102fcbf9c8b_uniq UNIQUE (old_path, site_id);


--
-- Name: wagtailredirects_redirect_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirects_redirect_pkey PRIMARY KEY (id);


--
-- Name: wagtailsearch_editorspick_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailsearch_editorspick
    ADD CONSTRAINT wagtailsearch_editorspick_pkey PRIMARY KEY (id);


--
-- Name: wagtailsearch_query_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailsearch_query
    ADD CONSTRAINT wagtailsearch_query_pkey PRIMARY KEY (id);


--
-- Name: wagtailsearch_query_query_string_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailsearch_query
    ADD CONSTRAINT wagtailsearch_query_query_string_key UNIQUE (query_string);


--
-- Name: wagtailsearch_querydailyhits_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailsearch_querydailyhits
    ADD CONSTRAINT wagtailsearch_querydailyhits_pkey PRIMARY KEY (id);


--
-- Name: wagtailsearch_querydailyhits_query_id_4e12c633921cb0c9_uniq; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailsearch_querydailyhits
    ADD CONSTRAINT wagtailsearch_querydailyhits_query_id_4e12c633921cb0c9_uniq UNIQUE (query_id, date);


--
-- Name: wagtailusers_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_pkey PRIMARY KEY (id);


--
-- Name: wagtailusers_userprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: pari; Tablespace: 
--

ALTER TABLE ONLY wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_user_id_key UNIQUE (user_id);


--
-- Name: album_albumslide_1a63c800; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX album_albumslide_1a63c800 ON album_albumslide USING btree (page_id);


--
-- Name: album_albumslide_f33175e6; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX album_albumslide_f33175e6 ON album_albumslide USING btree (image_id);


--
-- Name: article_article_authors_4f331e2f; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX article_article_authors_4f331e2f ON article_article_authors USING btree (author_id);


--
-- Name: article_article_authors_a00c1b00; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX article_article_authors_a00c1b00 ON article_article_authors USING btree (article_id);


--
-- Name: article_article_categories_a00c1b00; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX article_article_categories_a00c1b00 ON article_article_categories USING btree (article_id);


--
-- Name: article_article_categories_b583a629; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX article_article_categories_b583a629 ON article_article_categories USING btree (category_id);


--
-- Name: article_article_cdbc3e64; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX article_article_cdbc3e64 ON article_article USING btree (featured_image_id);


--
-- Name: article_article_locations_a00c1b00; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX article_article_locations_a00c1b00 ON article_article_locations USING btree (article_id);


--
-- Name: article_article_locations_e274a5da; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX article_article_locations_e274a5da ON article_article_locations USING btree (location_id);


--
-- Name: article_article_translators_4f331e2f; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX article_article_translators_4f331e2f ON article_article_translators USING btree (author_id);


--
-- Name: article_article_translators_a00c1b00; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX article_article_translators_a00c1b00 ON article_article_translators USING btree (article_id);


--
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: author_author_2dbcba41; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX author_author_2dbcba41 ON author_author USING btree (slug);


--
-- Name: author_author_f33175e6; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX author_author_f33175e6 ON author_author USING btree (image_id);


--
-- Name: author_author_name_190c26ab3ef157ec_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX author_author_name_190c26ab3ef157ec_like ON author_author USING btree (name varchar_pattern_ops);


--
-- Name: author_author_slug_50bb4523a4dcbd84_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX author_author_slug_50bb4523a4dcbd84_like ON author_author USING btree (slug varchar_pattern_ops);


--
-- Name: category_category_f33175e6; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX category_category_f33175e6 ON category_category USING btree (image_id);


--
-- Name: category_category_name_41a55a8c09ea040e_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX category_category_name_41a55a8c09ea040e_like ON category_category USING btree (name varchar_pattern_ops);


--
-- Name: core_affiximage_0a1a4dd8; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximage_0a1a4dd8 ON core_affiximage USING btree (collection_id);


--
-- Name: core_affiximage_categories_43accade; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximage_categories_43accade ON core_affiximage_categories USING btree (affiximage_id);


--
-- Name: core_affiximage_categories_b583a629; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximage_categories_b583a629 ON core_affiximage_categories USING btree (category_id);


--
-- Name: core_affiximage_created_at_4cf0a6940227ff57_uniq; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximage_created_at_4cf0a6940227ff57_uniq ON core_affiximage USING btree (created_at);


--
-- Name: core_affiximage_ef01e2b6; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximage_ef01e2b6 ON core_affiximage USING btree (uploaded_by_user_id);


--
-- Name: core_affiximage_locations_43accade; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximage_locations_43accade ON core_affiximage_locations USING btree (affiximage_id);


--
-- Name: core_affiximage_locations_e274a5da; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximage_locations_e274a5da ON core_affiximage_locations USING btree (location_id);


--
-- Name: core_affiximage_photographers_43accade; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximage_photographers_43accade ON core_affiximage_photographers USING btree (affiximage_id);


--
-- Name: core_affiximage_photographers_4f331e2f; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximage_photographers_4f331e2f ON core_affiximage_photographers USING btree (author_id);


--
-- Name: core_affiximagerendition_0a317463; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximagerendition_0a317463 ON core_affiximagerendition USING btree (filter_id);


--
-- Name: core_affiximagerendition_f33175e6; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_affiximagerendition_f33175e6 ON core_affiximagerendition USING btree (image_id);


--
-- Name: core_homepage_04f96ae3; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_04f96ae3 ON core_homepage USING btree (carousel_0_id);


--
-- Name: core_homepage_5280a83c; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_5280a83c ON core_homepage USING btree (carousel_1_id);


--
-- Name: core_homepage_738a4e3a; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_738a4e3a ON core_homepage USING btree (carousel_3_id);


--
-- Name: core_homepage_b9cada81; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_b9cada81 ON core_homepage USING btree (carousel_7_id);


--
-- Name: core_homepage_c0e96e59; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_c0e96e59 ON core_homepage USING btree (carousel_5_id);


--
-- Name: core_homepage_c59742f9; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_c59742f9 ON core_homepage USING btree (carousel_9_id);


--
-- Name: core_homepage_db79a56a; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_db79a56a ON core_homepage USING btree (carousel_8_id);


--
-- Name: core_homepage_e33c123d; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_e33c123d ON core_homepage USING btree (carousel_6_id);


--
-- Name: core_homepage_e37b472b; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_e37b472b ON core_homepage USING btree (carousel_4_id);


--
-- Name: core_homepage_fde5045d; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX core_homepage_fde5045d ON core_homepage USING btree (carousel_2_id);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: face_face_e274a5da; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX face_face_e274a5da ON face_face USING btree (location_id);


--
-- Name: face_face_f33175e6; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX face_face_f33175e6 ON face_face USING btree (image_id);


--
-- Name: location_location_2dbcba41; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX location_location_2dbcba41 ON location_location USING btree (slug);


--
-- Name: location_location_point_id; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX location_location_point_id ON location_location USING gist (point);


--
-- Name: location_location_slug_318b2a70082efd20_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX location_location_slug_318b2a70082efd20_like ON location_location USING btree (slug varchar_pattern_ops);


--
-- Name: resources_resource_categories_b583a629; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX resources_resource_categories_b583a629 ON resources_resource_categories USING btree (category_id);


--
-- Name: resources_resource_categories_e2f3ef5b; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX resources_resource_categories_e2f3ef5b ON resources_resource_categories USING btree (resource_id);


--
-- Name: taggit_tag_name_4ed9aad194b72af1_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX taggit_tag_name_4ed9aad194b72af1_like ON taggit_tag USING btree (name varchar_pattern_ops);


--
-- Name: taggit_tag_slug_703438030cd922a7_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX taggit_tag_slug_703438030cd922a7_like ON taggit_tag USING btree (slug varchar_pattern_ops);


--
-- Name: taggit_taggeditem_417f1b1c; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX taggit_taggeditem_417f1b1c ON taggit_taggeditem USING btree (content_type_id);


--
-- Name: taggit_taggeditem_76f094bc; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX taggit_taggeditem_76f094bc ON taggit_taggeditem USING btree (tag_id);


--
-- Name: taggit_taggeditem_af31437c; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX taggit_taggeditem_af31437c ON taggit_taggeditem USING btree (object_id);


--
-- Name: taggit_taggeditem_content_type_id_3c99b32018cc9d40_idx; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX taggit_taggeditem_content_type_id_3c99b32018cc9d40_idx ON taggit_taggeditem USING btree (content_type_id, object_id);


--
-- Name: wagtailcore_collection_path_fb7af1cc8ed8c35_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_collection_path_fb7af1cc8ed8c35_like ON wagtailcore_collection USING btree (path varchar_pattern_ops);


--
-- Name: wagtailcore_groupcollectionpermission_0a1a4dd8; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_groupcollectionpermission_0a1a4dd8 ON wagtailcore_groupcollectionpermission USING btree (collection_id);


--
-- Name: wagtailcore_groupcollectionpermission_0e939a4f; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_groupcollectionpermission_0e939a4f ON wagtailcore_groupcollectionpermission USING btree (group_id);


--
-- Name: wagtailcore_groupcollectionpermission_8373b171; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_groupcollectionpermission_8373b171 ON wagtailcore_groupcollectionpermission USING btree (permission_id);


--
-- Name: wagtailcore_grouppagepermission_0e939a4f; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_grouppagepermission_0e939a4f ON wagtailcore_grouppagepermission USING btree (group_id);


--
-- Name: wagtailcore_grouppagepermission_1a63c800; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_grouppagepermission_1a63c800 ON wagtailcore_grouppagepermission USING btree (page_id);


--
-- Name: wagtailcore_page_2dbcba41; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_page_2dbcba41 ON wagtailcore_page USING btree (slug);


--
-- Name: wagtailcore_page_417f1b1c; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_page_417f1b1c ON wagtailcore_page USING btree (content_type_id);


--
-- Name: wagtailcore_page_5e7b1936; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_page_5e7b1936 ON wagtailcore_page USING btree (owner_id);


--
-- Name: wagtailcore_page_first_published_at_785096aa58388042_uniq; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_page_first_published_at_785096aa58388042_uniq ON wagtailcore_page USING btree (first_published_at);


--
-- Name: wagtailcore_page_path_adbf7302a1ab75e_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_page_path_adbf7302a1ab75e_like ON wagtailcore_page USING btree (path varchar_pattern_ops);


--
-- Name: wagtailcore_page_slug_de66a236c47d916_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_page_slug_de66a236c47d916_like ON wagtailcore_page USING btree (slug varchar_pattern_ops);


--
-- Name: wagtailcore_page_submitted_for_moderation_10bec949f0821f20_uniq; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_page_submitted_for_moderation_10bec949f0821f20_uniq ON wagtailcore_pagerevision USING btree (submitted_for_moderation);


--
-- Name: wagtailcore_pagerevision_1a63c800; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_pagerevision_1a63c800 ON wagtailcore_pagerevision USING btree (page_id);


--
-- Name: wagtailcore_pagerevision_e8701ad4; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_pagerevision_e8701ad4 ON wagtailcore_pagerevision USING btree (user_id);


--
-- Name: wagtailcore_pageviewrestriction_1a63c800; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_pageviewrestriction_1a63c800 ON wagtailcore_pageviewrestriction USING btree (page_id);


--
-- Name: wagtailcore_site_0897acf4; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_site_0897acf4 ON wagtailcore_site USING btree (hostname);


--
-- Name: wagtailcore_site_8372b497; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_site_8372b497 ON wagtailcore_site USING btree (root_page_id);


--
-- Name: wagtailcore_site_hostname_3649a8ca5c8e8730_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailcore_site_hostname_3649a8ca5c8e8730_like ON wagtailcore_site USING btree (hostname varchar_pattern_ops);


--
-- Name: wagtaildocs_document_0a1a4dd8; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtaildocs_document_0a1a4dd8 ON wagtaildocs_document USING btree (collection_id);


--
-- Name: wagtaildocs_document_ef01e2b6; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtaildocs_document_ef01e2b6 ON wagtaildocs_document USING btree (uploaded_by_user_id);


--
-- Name: wagtailforms_formsubmission_1a63c800; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailforms_formsubmission_1a63c800 ON wagtailforms_formsubmission USING btree (page_id);


--
-- Name: wagtailimages_image_0a1a4dd8; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailimages_image_0a1a4dd8 ON wagtailimages_image USING btree (collection_id);


--
-- Name: wagtailimages_image_created_at_1e91a237c16eaa71_uniq; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailimages_image_created_at_1e91a237c16eaa71_uniq ON wagtailimages_image USING btree (created_at);


--
-- Name: wagtailimages_image_ef01e2b6; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailimages_image_ef01e2b6 ON wagtailimages_image USING btree (uploaded_by_user_id);


--
-- Name: wagtailimages_rendition_0a317463; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailimages_rendition_0a317463 ON wagtailimages_rendition USING btree (filter_id);


--
-- Name: wagtailimages_rendition_f33175e6; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailimages_rendition_f33175e6 ON wagtailimages_rendition USING btree (image_id);


--
-- Name: wagtailredirects_redirect_2fd79f37; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailredirects_redirect_2fd79f37 ON wagtailredirects_redirect USING btree (redirect_page_id);


--
-- Name: wagtailredirects_redirect_9365d6e7; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailredirects_redirect_9365d6e7 ON wagtailredirects_redirect USING btree (site_id);


--
-- Name: wagtailredirects_redirect_old_path_579ecadc1434daf4_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailredirects_redirect_old_path_579ecadc1434daf4_like ON wagtailredirects_redirect USING btree (old_path varchar_pattern_ops);


--
-- Name: wagtailsearch_editorspick_0bbeda9c; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailsearch_editorspick_0bbeda9c ON wagtailsearch_editorspick USING btree (query_id);


--
-- Name: wagtailsearch_editorspick_1a63c800; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailsearch_editorspick_1a63c800 ON wagtailsearch_editorspick USING btree (page_id);


--
-- Name: wagtailsearch_query_query_string_a78010a1796bb04_like; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailsearch_query_query_string_a78010a1796bb04_like ON wagtailsearch_query USING btree (query_string varchar_pattern_ops);


--
-- Name: wagtailsearch_querydailyhits_0bbeda9c; Type: INDEX; Schema: public; Owner: pari; Tablespace: 
--

CREATE INDEX wagtailsearch_querydailyhits_0bbeda9c ON wagtailsearch_querydailyhits USING btree (query_id);


--
-- Name: album_album_page_id_3eb242c31ea8562f_fk_album_album_page_ptr_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY album_albumslide
    ADD CONSTRAINT album_album_page_id_3eb242c31ea8562f_fk_album_album_page_ptr_id FOREIGN KEY (page_id) REFERENCES album_album(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: album_album_page_ptr_id_6eb82fb750d870f6_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY album_album
    ADD CONSTRAINT album_album_page_ptr_id_6eb82fb750d870f6_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: album_albumslid_image_id_1a3e874b54bafa20_fk_core_affiximage_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY album_albumslide
    ADD CONSTRAINT album_albumslid_image_id_1a3e874b54bafa20_fk_core_affiximage_id FOREIGN KEY (image_id) REFERENCES core_affiximage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: arti_article_id_536cd1eb57890e5f_fk_article_article_page_ptr_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_categories
    ADD CONSTRAINT arti_article_id_536cd1eb57890e5f_fk_article_article_page_ptr_id FOREIGN KEY (article_id) REFERENCES article_article(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: arti_article_id_795ecc6887f156f7_fk_article_article_page_ptr_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_translators
    ADD CONSTRAINT arti_article_id_795ecc6887f156f7_fk_article_article_page_ptr_id FOREIGN KEY (article_id) REFERENCES article_article(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: artic_article_id_604897b170751e8_fk_article_article_page_ptr_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_authors
    ADD CONSTRAINT artic_article_id_604897b170751e8_fk_article_article_page_ptr_id FOREIGN KEY (article_id) REFERENCES article_article(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: artic_article_id_8613cf48640b6de_fk_article_article_page_ptr_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_locations
    ADD CONSTRAINT artic_article_id_8613cf48640b6de_fk_article_article_page_ptr_id FOREIGN KEY (article_id) REFERENCES article_article(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: articl_featured_image_id_44bb78414de2c456_fk_core_affiximage_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article
    ADD CONSTRAINT articl_featured_image_id_44bb78414de2c456_fk_core_affiximage_id FOREIGN KEY (featured_image_id) REFERENCES core_affiximage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: article_ar_category_id_3179c33ce65ca930_fk_category_category_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_categories
    ADD CONSTRAINT article_ar_category_id_3179c33ce65ca930_fk_category_category_id FOREIGN KEY (category_id) REFERENCES category_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: article_art_location_id_6c129d2c4c2e762_fk_location_location_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_locations
    ADD CONSTRAINT article_art_location_id_6c129d2c4c2e762_fk_location_location_id FOREIGN KEY (location_id) REFERENCES location_location(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: article_art_page_ptr_id_4e08dc27c9cffad2_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article
    ADD CONSTRAINT article_art_page_ptr_id_4e08dc27c9cffad2_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: article_article__author_id_3595d330bac0e9bb_fk_author_author_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_translators
    ADD CONSTRAINT article_article__author_id_3595d330bac0e9bb_fk_author_author_id FOREIGN KEY (author_id) REFERENCES author_author(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: article_article__author_id_619b102ff99bb29a_fk_author_author_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY article_article_authors
    ADD CONSTRAINT article_article__author_id_619b102ff99bb29a_fk_author_author_id FOREIGN KEY (author_id) REFERENCES author_author(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: author_author_image_id_7220e2a124dd5828_fk_core_affiximage_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY author_author
    ADD CONSTRAINT author_author_image_id_7220e2a124dd5828_fk_core_affiximage_id FOREIGN KEY (image_id) REFERENCES core_affiximage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: category_catego_image_id_4823f32a1723f816_fk_core_affiximage_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY category_category
    ADD CONSTRAINT category_catego_image_id_4823f32a1723f816_fk_core_affiximage_id FOREIGN KEY (image_id) REFERENCES core_affiximage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cor_collection_id_522385563aea4d62_fk_wagtailcore_collection_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage
    ADD CONSTRAINT cor_collection_id_522385563aea4d62_fk_wagtailcore_collection_id FOREIGN KEY (collection_id) REFERENCES wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_affi_filter_id_5d081ca5a41a8ba1_fk_wagtailimages_filter_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximagerendition
    ADD CONSTRAINT core_affi_filter_id_5d081ca5a41a8ba1_fk_wagtailimages_filter_id FOREIGN KEY (filter_id) REFERENCES wagtailimages_filter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_affix_affiximage_id_58a82e30bb32e4fb_fk_core_affiximage_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage_categories
    ADD CONSTRAINT core_affix_affiximage_id_58a82e30bb32e4fb_fk_core_affiximage_id FOREIGN KEY (affiximage_id) REFERENCES core_affiximage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_affix_affiximage_id_7753e397c9e433b4_fk_core_affiximage_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage_locations
    ADD CONSTRAINT core_affix_affiximage_id_7753e397c9e433b4_fk_core_affiximage_id FOREIGN KEY (affiximage_id) REFERENCES core_affiximage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_affix_category_id_258667b55365c630_fk_category_category_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage_categories
    ADD CONSTRAINT core_affix_category_id_258667b55365c630_fk_category_category_id FOREIGN KEY (category_id) REFERENCES category_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_affix_location_id_2213fe5459b0ca62_fk_location_location_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage_locations
    ADD CONSTRAINT core_affix_location_id_2213fe5459b0ca62_fk_location_location_id FOREIGN KEY (location_id) REFERENCES location_location(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_affix_uploaded_by_user_id_79c6906edfe0d76e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage
    ADD CONSTRAINT core_affix_uploaded_by_user_id_79c6906edfe0d76e_fk_auth_user_id FOREIGN KEY (uploaded_by_user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_affixi_affiximage_id_a6168fd44e9d840_fk_core_affiximage_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage_photographers
    ADD CONSTRAINT core_affixi_affiximage_id_a6168fd44e9d840_fk_core_affiximage_id FOREIGN KEY (affiximage_id) REFERENCES core_affiximage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_affiximage__author_id_2a36715014a18cf8_fk_author_author_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximage_photographers
    ADD CONSTRAINT core_affiximage__author_id_2a36715014a18cf8_fk_author_author_id FOREIGN KEY (author_id) REFERENCES author_author(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_affiximage_image_id_77108fc949b9a8d3_fk_core_affiximage_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_affiximagerendition
    ADD CONSTRAINT core_affiximage_image_id_77108fc949b9a8d3_fk_core_affiximage_id FOREIGN KEY (image_id) REFERENCES core_affiximage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_0_id_42ecef2a11b0d8aa_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_0_id_42ecef2a11b0d8aa_fk_wagtailcore_page_id FOREIGN KEY (carousel_0_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_1_id_41d74d3a1ce6ca3d_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_1_id_41d74d3a1ce6ca3d_fk_wagtailcore_page_id FOREIGN KEY (carousel_1_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_2_id_6793d3d08de416c0_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_2_id_6793d3d08de416c0_fk_wagtailcore_page_id FOREIGN KEY (carousel_2_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_3_id_53dd74ebf698f4cb_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_3_id_53dd74ebf698f4cb_fk_wagtailcore_page_id FOREIGN KEY (carousel_3_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_4_id_6957d219e1c1f09e_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_4_id_6957d219e1c1f09e_fk_wagtailcore_page_id FOREIGN KEY (carousel_4_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_5_id_641d062c71380f81_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_5_id_641d062c71380f81_fk_wagtailcore_page_id FOREIGN KEY (carousel_5_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_6_id_61809b9d4d6b7eec_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_6_id_61809b9d4d6b7eec_fk_wagtailcore_page_id FOREIGN KEY (carousel_6_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_7_id_4acce2824745e95f_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_7_id_4acce2824745e95f_fk_wagtailcore_page_id FOREIGN KEY (carousel_7_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_8_id_7753451abed25af2_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_8_id_7753451abed25af2_fk_wagtailcore_page_id FOREIGN KEY (carousel_8_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_home_carousel_9_id_2d2158d341e789a5_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_home_carousel_9_id_2d2158d341e789a5_fk_wagtailcore_page_id FOREIGN KEY (carousel_9_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_homepag_page_ptr_id_2f2f136054b7e53_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_homepage
    ADD CONSTRAINT core_homepag_page_ptr_id_2f2f136054b7e53_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_static_page_ptr_id_11bd5b97a7bf5308_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY core_staticpage
    ADD CONSTRAINT core_static_page_ptr_id_11bd5b97a7bf5308_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: face_face_image_id_4c5a4bcef969498_fk_core_affiximage_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY face_face
    ADD CONSTRAINT face_face_image_id_4c5a4bcef969498_fk_core_affiximage_id FOREIGN KEY (image_id) REFERENCES core_affiximage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: face_face_location_id_63e88db1e0246799_fk_location_location_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY face_face
    ADD CONSTRAINT face_face_location_id_63e88db1e0246799_fk_location_location_id FOREIGN KEY (location_id) REFERENCES location_location(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: face_face_page_ptr_id_280681c1548277e0_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY face_face
    ADD CONSTRAINT face_face_page_ptr_id_280681c1548277e0_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: resource_id_71337e832d2539d2_fk_resources_resource_page_ptr_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY resources_resource_categories
    ADD CONSTRAINT resource_id_71337e832d2539d2_fk_resources_resource_page_ptr_id FOREIGN KEY (resource_id) REFERENCES resources_resource(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: resources__category_id_353e842cb3cd96fe_fk_category_category_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY resources_resource_categories
    ADD CONSTRAINT resources__category_id_353e842cb3cd96fe_fk_category_category_id FOREIGN KEY (category_id) REFERENCES category_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: resources_r_page_ptr_id_30c0d30eda7b60a8_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY resources_resource
    ADD CONSTRAINT resources_r_page_ptr_id_30c0d30eda7b60a8_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tagg_content_type_id_62e0524705c3ec8f_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY taggit_taggeditem
    ADD CONSTRAINT tagg_content_type_id_62e0524705c3ec8f_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: taggit_taggeditem_tag_id_6318217c0d95e0d2_fk_taggit_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_tag_id_6318217c0d95e0d2_fk_taggit_tag_id FOREIGN KEY (tag_id) REFERENCES taggit_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wag_collection_id_1b29a2a37e7d436c_fk_wagtailcore_collection_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wag_collection_id_1b29a2a37e7d436c_fk_wagtailcore_collection_id FOREIGN KEY (collection_id) REFERENCES wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wag_collection_id_285e87239b035e6a_fk_wagtailcore_collection_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailimages_image
    ADD CONSTRAINT wag_collection_id_285e87239b035e6a_fk_wagtailcore_collection_id FOREIGN KEY (collection_id) REFERENCES wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wag_collection_id_2b616eaa03011e90_fk_wagtailcore_collection_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtaildocs_document
    ADD CONSTRAINT wag_collection_id_2b616eaa03011e90_fk_wagtailcore_collection_id FOREIGN KEY (collection_id) REFERENCES wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagt_content_type_id_7ae0ebb2acb1454e_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_page
    ADD CONSTRAINT wagt_content_type_id_7ae0ebb2acb1454e_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtai_redirect_page_id_4fb5deae195b3223_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailredirects_redirect
    ADD CONSTRAINT wagtai_redirect_page_id_4fb5deae195b3223_fk_wagtailcore_page_id FOREIGN KEY (redirect_page_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcor_permission_id_48aff6f1dd268787_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcor_permission_id_48aff6f1dd268787_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcor_root_page_id_5c8b4b84e03f7f29_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_site
    ADD CONSTRAINT wagtailcor_root_page_id_5c8b4b84e03f7f29_fk_wagtailcore_page_id FOREIGN KEY (root_page_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_gro_page_id_70d2788c0579bb7c_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_gro_page_id_70d2788c0579bb7c_fk_wagtailcore_page_id FOREIGN KEY (page_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_groupcol_group_id_6d27de27630f0e7a_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_group_id_6d27de27630f0e7a_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_grouppage_group_id_2df9571b92fb26d_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppage_group_id_2df9571b92fb26d_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_pag_page_id_1d5ab1303676feba_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_pagerevision
    ADD CONSTRAINT wagtailcore_pag_page_id_1d5ab1303676feba_fk_wagtailcore_page_id FOREIGN KEY (page_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_pag_page_id_318895e696da7fed_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_pageviewrestriction
    ADD CONSTRAINT wagtailcore_pag_page_id_318895e696da7fed_fk_wagtailcore_page_id FOREIGN KEY (page_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_page_owner_id_7a2f24f1767b30bc_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_owner_id_7a2f24f1767b30bc_fk_auth_user_id FOREIGN KEY (owner_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_pagerevisi_user_id_3a9a8cf31a218402_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailcore_pagerevision
    ADD CONSTRAINT wagtailcore_pagerevisi_user_id_3a9a8cf31a218402_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtaildoc_uploaded_by_user_id_62c5d96169f4ec20_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtaildocs_document
    ADD CONSTRAINT wagtaildoc_uploaded_by_user_id_62c5d96169f4ec20_fk_auth_user_id FOREIGN KEY (uploaded_by_user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailforms_fo_page_id_72bcec1db96e6d21_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailforms_formsubmission
    ADD CONSTRAINT wagtailforms_fo_page_id_72bcec1db96e6d21_fk_wagtailcore_page_id FOREIGN KEY (page_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailima_filter_id_b5a94d704fa1f7f_fk_wagtailimages_filter_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailimages_rendition
    ADD CONSTRAINT wagtailima_filter_id_b5a94d704fa1f7f_fk_wagtailimages_filter_id FOREIGN KEY (filter_id) REFERENCES wagtailimages_filter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailima_uploaded_by_user_id_4941ddafe7e6985a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailimages_image
    ADD CONSTRAINT wagtailima_uploaded_by_user_id_4941ddafe7e6985a_fk_auth_user_id FOREIGN KEY (uploaded_by_user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailimag_image_id_4b83f0a74ebd24db_fk_wagtailimages_image_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailimages_rendition
    ADD CONSTRAINT wagtailimag_image_id_4b83f0a74ebd24db_fk_wagtailimages_image_id FOREIGN KEY (image_id) REFERENCES wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailredirect_site_id_72075f3bbfcf92e7_fk_wagtailcore_site_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailredirects_redirect
    ADD CONSTRAINT wagtailredirect_site_id_72075f3bbfcf92e7_fk_wagtailcore_site_id FOREIGN KEY (site_id) REFERENCES wagtailcore_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailsear_query_id_355494074ca8351a_fk_wagtailsearch_query_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailsearch_querydailyhits
    ADD CONSTRAINT wagtailsear_query_id_355494074ca8351a_fk_wagtailsearch_query_id FOREIGN KEY (query_id) REFERENCES wagtailsearch_query(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailsear_query_id_74051b390c9e69bd_fk_wagtailsearch_query_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailsearch_editorspick
    ADD CONSTRAINT wagtailsear_query_id_74051b390c9e69bd_fk_wagtailsearch_query_id FOREIGN KEY (query_id) REFERENCES wagtailsearch_query(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailsearch_e_page_id_3cd69b3b50c44c9b_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailsearch_editorspick
    ADD CONSTRAINT wagtailsearch_e_page_id_3cd69b3b50c44c9b_fk_wagtailcore_page_id FOREIGN KEY (page_id) REFERENCES wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailusers_userprofi_user_id_755efda9998dba71_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pari
--

ALTER TABLE ONLY wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofi_user_id_755efda9998dba71_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

