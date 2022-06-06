def session_commit_rollback_close(session):
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        