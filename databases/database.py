from neo4j import GraphDatabase

from settings import get_settings

neo4j_driver = GraphDatabase.driver(
    uri=get_settings().NEO4J_URI,
    auth=(get_settings().NEO4J_USER, get_settings().NEO4J_PASSWORD),
    database=get_settings().NEO4J_DATABASE,
)