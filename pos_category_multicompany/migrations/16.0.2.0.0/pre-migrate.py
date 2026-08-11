def migrate(cr, version):
    if not version:
        return
    # Creamos una tabla temporal con los datos de company_id
    cr.execute(
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name='pos_category' AND column_name='company_id'
        """
    )
    column_exists_company_id = cr.fetchone()
    if column_exists_company_id:
        # Odoo relanza la migracion en cada update mientras el modulo no llegue
        # a 16.0.2.0.0. Si un intento previo dejo la temporal a medias, un
        # CREATE IF NOT EXISTS acumularia las mismas filas otra vez.
        cr.execute(
            """
            DROP TABLE IF EXISTS company_id_rel_legacy;
            """
        )
        cr.execute(
            """
            CREATE TABLE company_id_rel_legacy (
                pos_category_id INT NOT NULL,
                company_id INT NOT NULL
            );
            """
        )
        cr.execute(
            """
            INSERT INTO company_id_rel_legacy (pos_category_id, company_id)
            SELECT id, company_id
            FROM pos_category
            WHERE company_id IS NOT NULL;
            """
        )
