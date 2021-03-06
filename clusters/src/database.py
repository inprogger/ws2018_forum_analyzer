import psycopg2
from src.database import get_connect


def count_clusters(url_id):
    """
        Подсчет количества текстов в каждом кластере
        Возвращает описание кластера и количество текство в нем

    """
    connect = get_connect()

    cursor = connect.cursor()
    cursor.execute(
        "SELECT cluster.id, cluster.summary, cluster.image, count(*) "
        "FROM clusters_cluster AS cluster "
        "INNER JOIN texts_text AS text "
            "ON cluster.id = text.cluster_id "
        "INNER JOIN texts_url AS url "
            "ON text.url_id = url.id "
        "WHERE url.id = {} "
        "GROUP BY cluster.summary, cluster.id;".format(url_id)
    )

    clusters = cursor.fetchall()
    connect.close()

    return clusters


def get_image_url_by_id(url_id):
    """
        Подсчет количества текстов в каждом кластере
        Возвращает описание кластера и количество текство в нем

    """
    connect = get_connect()

    cursor = connect.cursor()
    cursor.execute(
        "SELECT url.image "
        "FROM texts_url AS url "
        "WHERE url.id = {} ".format(url_id)
    )

    clusters = cursor.fetchall()
    connect.close()

    return clusters


def cluster_of_text(text_id):
    """
        Получаем кластер по идентификатору текста

    """
    connect = get_connect()

    cursor = connect.cursor()
    cursor.execute(
        "SELECT cluster.id, cluster.summary "
        "FROM clusters_cluster AS cluster "
        "INNER JOIN texts_text AS text "
        "ON text.cluster_id = cluster.id "
        "WHERE text.id = {}".format(text_id)
    )
    cluster = cursor.fetchall()
    connect.close()

    return cluster


if __name__ == '__main__':
    pass