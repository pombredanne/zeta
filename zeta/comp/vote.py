# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to access data base and do data-crunching on vote tables.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
#   1. Since voting is a horizontal feature, the permissions for casting and
#      viewing votes are delegated to the corresponding components.
# Todo    : None
#   1. Figure out a way to identify the `modelobj` for logging purpose.

from   __future__              import with_statement

from   sqlalchemy              import *
from   sqlalchemy.orm          import *

import zeta.lib.helpers        as h
from   zeta.ccore              import Component
from   zeta.model              import meta
from   zeta.model.schema       import t_wikipage, t_vote
from   zeta.model.tables       import Vote, Ticket

tbl_mappers = meta.tbl_mappers
metadata    = meta.metadata

from   zeta.ccore              import Component

class VoteComponent( Component ) :
    def cast_vote( self, voter, modelobj=None, votedas='', medium='' ) :
        """Cast a vote for `voter`, which can be,
            `user_id`, `username` or User instance"""
        from zeta.config.environment import userscomp

        voter     = userscomp.get_user( voter )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            vote = Vote()
            votedas and setattr( vote, 'votedas', votedas )
            medium  and setattr( vote, 'medium', medium )
            vote.voter = voter
            msession.add( vote )
            voter.votes.append( vote )
            modelobj and modelobj.votes.append( vote )

    def recast_vote( self, vote, votedas='', medium='' ) :
        """Cast a vote for `voter`, which can be,
            `user_id`, `username` or User instance"""
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            if vote and votedas :
                vote.votedas = votedas
            medium  and setattr( vote, 'medium', medium )

    def remove_vote( self, vote ) :
        """Remove the specified vote"""
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            msession.delete( vote )

    def ticketvotes( self, ticket, votedas='', medium='' ) :
        """count the votes for 'ticket' with specified `votedas` and `medium`
        values."""
        msession  = meta.Session()
        q = msession.query( Vote ).join('ticket').filter_by( id=ticket.id )
        if votedas :
            q = q.filter( Vote.votedas==votedas )
        if medium :
            q = q.filter( Vote.medium==medium )
        return q.all()

    def wikivotes( self, wiki, votedas='', medium='' ) :
        """count the votes for 'wiki' with specified `votedas` and `medium`
        values."""
        msession  = meta.Session()
        q = msession.query( Vote ).join( 'wiki').filter_by( id=wiki.id )
        if votedas :
            q = q.filter( Vote.votedas==votedas )
        if medium :
            q = q.filter( Vote.medium==medium )
        return q.all()

    def get_ticketvote( self, voter=None, ticket=None ) :
        """Get the vote with specific attribute"""
        from zeta.config.environment import userscomp

        voter     = voter and userscomp.get_user( voter )
        msession = meta.Session()
        if voter and ticket :
            vote = msession.query( Vote ).join( 'ticket' 
                   ).filter_by( id=ticket.id ).filter( Vote.user_id==voter.id ).first()
        elif ticket :
            vote = msession.query( Vote ).join( 'ticket' 
                   ).filter_by( id=ticket.id ).all()
        else :
            vote = msession.query( Vote ).all()
        return vote

    def get_wikivote( self, voter=None, wiki=None ) :
        """Get the vote with specific attribute"""
        from zeta.config.environment import userscomp

        voter     = voter and userscomp.get_user( voter )
        msession = meta.Session()
        if voter and wiki :
            vote = msession.query( Vote ).join( 'wiki' 
                   ).filter_by( id=wiki.id ).filter( Vote.user_id==voter.id ).first()
        elif wiki :
            vote = msession.query( Vote ).join( 'wiki' 
                   ).filter_by( id=wiki.id ).all()
        else :
            vote = msession.query( Vote ).all()
        return vote

    def get_vote( self, voter=None ) :
        """Get all the votes casted by the user"""
        from zeta.config.environment import userscomp

        voter     = voter and userscomp.get_user( voter )
        msession  = meta.Session()
        if voter :
            vote = msession.query( Vote ).filter( Vote.user_id==voter.id ).all()
        else :
            vote = msession.query( Vote ).all()
        return vote

    # Data Crunching methods on vote database.

    def uservotes( self, user ) :
        """Count and analyse all the votes casted by `user`"""
        q  = select( [ t_vote.c.id, t_vote.c.votedas, t_vote.c.medium,
                       t_vote.c.created_on,
                     ],
                     bind=meta.engine
                   ).where( t_vote.c.user_id == user.id )
        votes = {}
        for tup in q.execute().fetchall() :
            if tup[0] == None : continue
            votes.setdefault( tup[1], [] ).append( tup )
        return votes

    # Vote component properties
