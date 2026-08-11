def migrate(cr, version):
    if not version:
        return
    # Insertamos los datos a la tabla
    # company_id_rel_legacy con los datos de la tabla temporal
    cr.execute(
        """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'company_id_rel_legacy'
        );
        """
    )
    exists_company_id_rel_legacy = cr.fetchone()[0]
    if exists_company_id_rel_legacy:
        # pos_category_company_rel puede sobrevivir a un update fallido: la
        # tabla se comitea al crear el campo, pero latest_version solo se marca
        # al final. ON CONFLICT deja la migracion re-ejecutable.
        cr.execute(
            """
            INSERT INTO pos_category_company_rel (pos_category_id, res_company_id)
            SELECT pos_category_id, company_id
            FROM company_id_rel_legacy
            ON CONFLICT DO NOTHING;
            """
        )
        cr.execute(
            """
            DROP TABLE IF EXISTS company_id_rel_legacy;
            """
        )
