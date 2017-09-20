"""[Observations](https://github.com/edwardlib/observations) provides
a one line Python API for loading standard data sets in machine
learning. It automates the process from downloading, extracting,
loading, and preprocessing data. Observations helps keep the workflow
reproducible and follow sensible standards.

Observations is a standalone Python library and must be installed
separate from Edward.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from observations.rdata.air_passengers import air_passengers
from observations.rdata.bj_sales import bj_sales
from observations.rdata.bod import bod
from observations.rdata.co2 import co2
from observations.rdata.formaldehyde import formaldehyde
from observations.rdata.hair_eye_color import hair_eye_color
from observations.rdata.insect_sprays import insect_sprays
from observations.rdata.johnson_johnson import johnson_johnson
from observations.rdata.lake_huron import lake_huron
from observations.rdata.life_cycle_savings import life_cycle_savings
from observations.rdata.nile import nile
from observations.rdata.orchard_sprays import orchard_sprays
from observations.rdata.plant_growth import plant_growth
from observations.rdata.puromycin import puromycin
from observations.rdata.titanic import titanic
from observations.rdata.tooth_growth import tooth_growth
from observations.rdata.ucb_admissions import ucb_admissions
from observations.rdata.uk_driver_deaths import uk_driver_deaths
from observations.rdata.uk_gas import uk_gas
from observations.rdata.us_acc_deaths import us_acc_deaths
from observations.rdata.us_arrests import us_arrests
from observations.rdata.us_judge_ratings import us_judge_ratings
from observations.rdata.us_personal_expenditure import us_personal_expenditure
from observations.rdata.va_deaths import va_deaths
from observations.rdata.www_usage import www_usage
from observations.rdata.world_phones import world_phones
from observations.rdata.airmiles import airmiles
from observations.rdata.airquality import airquality
from observations.rdata.anscombe import anscombe
from observations.rdata.attenu import attenu
from observations.rdata.attitude import attitude
from observations.rdata.austres import austres
from observations.rdata.cars import cars
from observations.rdata.chickwts import chickwts
from observations.rdata.co2_1 import co2_1
from observations.rdata.crimtab import crimtab
from observations.rdata.discoveries import discoveries
from observations.rdata.esoph import esoph
from observations.rdata.euro import euro
from observations.rdata.faithful import faithful
from observations.rdata.freeny import freeny
from observations.rdata.infert import infert
from observations.rdata.iris import iris
from observations.rdata.islands import islands
from observations.rdata.lh import lh
from observations.rdata.longley import longley
from observations.rdata.lynx import lynx
from observations.rdata.morley import morley
from observations.rdata.mtcars import mtcars
from observations.rdata.nhtemp import nhtemp
from observations.rdata.nottem import nottem
from observations.rdata.npk import npk
from observations.rdata.occupational_status import occupational_status
from observations.rdata.precip import precip
from observations.rdata.presidents import presidents
from observations.rdata.pressure import pressure
from observations.rdata.quakes import quakes
from observations.rdata.randu import randu
from observations.rdata.rivers import rivers
from observations.rdata.rock import rock
from observations.rdata.sleep import sleep
from observations.rdata.stackloss import stackloss
from observations.rdata.sunspot_month import sunspot_month
from observations.rdata.sunspot_year import sunspot_year
from observations.rdata.sunspots import sunspots
from observations.rdata.swiss import swiss
from observations.rdata.treering import treering
from observations.rdata.trees import trees
from observations.rdata.uspop import uspop
from observations.rdata.volcano import volcano
from observations.rdata.warpbreaks import warpbreaks
from observations.rdata.women import women
from observations.rdata.acme import acme
from observations.rdata.aids import aids
from observations.rdata.aircondit import aircondit
from observations.rdata.aircondit7 import aircondit7
from observations.rdata.amis import amis
from observations.rdata.aml import aml
from observations.rdata.bigcity import bigcity
from observations.rdata.brambles import brambles
from observations.rdata.breslow import breslow
from observations.rdata.calcium import calcium
from observations.rdata.cane import cane
from observations.rdata.capability import capability
from observations.rdata.cats_m import cats_m
from observations.rdata.cav import cav
from observations.rdata.cd4 import cd4
from observations.rdata.channing import channing
from observations.rdata.city import city
from observations.rdata.claridge import claridge
from observations.rdata.cloth import cloth
from observations.rdata.co_transfer import co_transfer
from observations.rdata.coal import coal
from observations.rdata.darwin import darwin
from observations.rdata.dogs import dogs
from observations.rdata.downs_bc import downs_bc
from observations.rdata.ducks import ducks
from observations.rdata.fir import fir
from observations.rdata.frets import frets
from observations.rdata.grav import grav
from observations.rdata.gravity import gravity
from observations.rdata.hirose import hirose
from observations.rdata.islay import islay
from observations.rdata.manaus import manaus
from observations.rdata.melanoma import melanoma
from observations.rdata.motor import motor
from observations.rdata.neuro import neuro
from observations.rdata.nitrofen import nitrofen
from observations.rdata.nodal import nodal
from observations.rdata.nuclear import nuclear
from observations.rdata.paulsen import paulsen
from observations.rdata.poisons import poisons
from observations.rdata.polar import polar
from observations.rdata.remission import remission
from observations.rdata.salinity import salinity
from observations.rdata.survival import survival
from observations.rdata.tau import tau
from observations.rdata.tuna import tuna
from observations.rdata.urine import urine
from observations.rdata.wool import wool
from observations.rdata.acf1 import acf1
from observations.rdata.cars93_summary import cars93_summary
from observations.rdata.lottario import lottario
from observations.rdata.manitoba_lakes import manitoba_lakes
from observations.rdata.sp500_w90 import sp500_w90
from observations.rdata.sp500_close import sp500_close
from observations.rdata.ais import ais
from observations.rdata.allbacks import allbacks
from observations.rdata.anesthetic import anesthetic
from observations.rdata.ant111b import ant111b
from observations.rdata.antigua import antigua
from observations.rdata.appletaste import appletaste
from observations.rdata.aulatlong import aulatlong
from observations.rdata.austpop import austpop
from observations.rdata.biomass import biomass
from observations.rdata.bomregions import bomregions
from observations.rdata.bomregions2011 import bomregions2011
from observations.rdata.bomregions2012 import bomregions2012
from observations.rdata.bomsoi import bomsoi
from observations.rdata.bomsoi2001 import bomsoi2001
from observations.rdata.carprice import carprice
from observations.rdata.cerealsugar import cerealsugar
from observations.rdata.cfseal import cfseal
from observations.rdata.cities import cities
from observations.rdata.codling import codling
from observations.rdata.cottonworkers import cottonworkers
from observations.rdata.cps1 import cps1
from observations.rdata.cps2 import cps2
from observations.rdata.cps3 import cps3
from observations.rdata.cricketer import cricketer
from observations.rdata.cuckoohosts import cuckoohosts
from observations.rdata.cuckoos import cuckoos
from observations.rdata.dengue import dengue
from observations.rdata.dewpoint import dewpoint
from observations.rdata.droughts import droughts
from observations.rdata.edc_co2 import edc_co2
from observations.rdata.edc_t import edc_t
from observations.rdata.elastic1 import elastic1
from observations.rdata.elastic2 import elastic2
from observations.rdata.elasticband import elasticband
from observations.rdata.fossilfuel import fossilfuel
from observations.rdata.fossum import fossum
from observations.rdata.frogs import frogs
from observations.rdata.frostedflakes import frostedflakes
from observations.rdata.fruitohms import fruitohms
from observations.rdata.gaba import gaba
from observations.rdata.geophones import geophones
from observations.rdata.grog import grog
from observations.rdata.head_injury import head_injury
from observations.rdata.hills import hills
from observations.rdata.hills2000 import hills2000
from observations.rdata.hotspots import hotspots
from observations.rdata.hotspots2006 import hotspots2006
from observations.rdata.houseprices import houseprices
from observations.rdata.humanpower1 import humanpower1
from observations.rdata.humanpower2 import humanpower2
from observations.rdata.hurric_named import hurric_named
from observations.rdata.intersalt import intersalt
from observations.rdata.ironslag import ironslag
from observations.rdata.jobs import jobs
from observations.rdata.kiwishade import kiwishade
from observations.rdata.leafshape import leafshape
from observations.rdata.leafshape17 import leafshape17
from observations.rdata.leaftemp import leaftemp
from observations.rdata.leaftemp_all import leaftemp_all
from observations.rdata.litters import litters
from observations.rdata.lung import lung
from observations.rdata.measles import measles
from observations.rdata.med_expenses import med_expenses
from observations.rdata.mifem import mifem
from observations.rdata.mignonette import mignonette
from observations.rdata.milk import milk
from observations.rdata.modelcars import modelcars
from observations.rdata.monica import monica
from observations.rdata.moths import moths
from observations.rdata.nass_cds import nass_cds
from observations.rdata.nasshead import nasshead
from observations.rdata.nihills import nihills
from observations.rdata.nsw74demo import nsw74demo
from observations.rdata.nsw74psid1 import nsw74psid1
from observations.rdata.nsw74psid3 import nsw74psid3
from observations.rdata.nsw74psid_a import nsw74psid_a
from observations.rdata.nswdemo import nswdemo
from observations.rdata.nswpsid1 import nswpsid1
from observations.rdata.oddbooks import oddbooks
from observations.rdata.orings import orings
from observations.rdata.pair65 import pair65
from observations.rdata.possum import possum
from observations.rdata.possumsites import possumsites
from observations.rdata.primates import primates
from observations.rdata.progression import progression
from observations.rdata.psid1 import psid1
from observations.rdata.psid2 import psid2
from observations.rdata.psid3 import psid3
from observations.rdata.races2000 import races2000
from observations.rdata.rainforest import rainforest
from observations.rdata.rareplants import rareplants
from observations.rdata.rice import rice
from observations.rdata.rock_art import rock_art
from observations.rdata.roller import roller
from observations.rdata.science import science
from observations.rdata.seedrates import seedrates
from observations.rdata.socsupport import socsupport
from observations.rdata.softbacks import softbacks
from observations.rdata.sorption import sorption
from observations.rdata.spam7 import spam7
from observations.rdata.st_vincent import st_vincent
from observations.rdata.sugar import sugar
from observations.rdata.tinting import tinting
from observations.rdata.tomato import tomato
from observations.rdata.toycars import toycars
from observations.rdata.vince111b import vince111b
from observations.rdata.vlt import vlt
from observations.rdata.wages1833 import wages1833
from observations.rdata.world_records import world_records
from observations.rdata.fars import fars
from observations.rdata.air_accs import air_accs
from observations.rdata.cvalues import cvalues
from observations.rdata.fars2007 import fars2007
from observations.rdata.fars2008 import fars2008
from observations.rdata.german import german
from observations.rdata.loti import loti
from observations.rdata.alloauto import alloauto
from observations.rdata.allograft import allograft
from observations.rdata.azt import azt
from observations.rdata.baboon import baboon
from observations.rdata.bcdeter import bcdeter
from observations.rdata.bfeed import bfeed
from observations.rdata.bmt import bmt
from observations.rdata.bnct import bnct
from observations.rdata.btrial import btrial
from observations.rdata.burn import burn
from observations.rdata.drug6mp import drug6mp
from observations.rdata.drughiv import drughiv
from observations.rdata.hodg import hodg
from observations.rdata.kidrecurr import kidrecurr
from observations.rdata.kidtran import kidtran
from observations.rdata.larynx import larynx
from observations.rdata.pneumon import pneumon
from observations.rdata.psych import psych
from observations.rdata.std import std
from observations.rdata.stddiag import stddiag
from observations.rdata.tongue import tongue
from observations.rdata.twins import twins
from observations.rdata.animals2 import animals2
from observations.rdata.crohn_d import crohn_d
from observations.rdata.n_ox_emissions import n_ox_emissions
from observations.rdata.siegels_ex import siegels_ex
from observations.rdata.aircraft import aircraft
from observations.rdata.airmay import airmay
from observations.rdata.alcohol import alcohol
from observations.rdata.ambient_noxch import ambient_noxch
from observations.rdata.biomass_till import biomass_till
from observations.rdata.bushfire import bushfire
from observations.rdata.carrots import carrots
from observations.rdata.cloud import cloud
from observations.rdata.coleman import coleman
from observations.rdata.condroz import condroz
from observations.rdata.cushny import cushny
from observations.rdata.delivery import delivery
from observations.rdata.education import education
from observations.rdata.epilepsy import epilepsy
from observations.rdata.ex_am import ex_am
from observations.rdata.foodstamp import foodstamp
from observations.rdata.hbk import hbk
from observations.rdata.heart import heart
from observations.rdata.kootenay import kootenay
from observations.rdata.lactic import lactic
from observations.rdata.pension import pension
from observations.rdata.phosphor import phosphor
from observations.rdata.pilot import pilot
from observations.rdata.possum_div import possum_div
from observations.rdata.pulpfiber import pulpfiber
from observations.rdata.radar_image import radar_image
from observations.rdata.stars_cyg import stars_cyg
from observations.rdata.telef import telef
from observations.rdata.toxicity import toxicity
from observations.rdata.vaso import vaso
from observations.rdata.wagner_growth import wagner_growth
from observations.rdata.wood import wood
from observations.rdata.ams_survey import ams_survey
from observations.rdata.adler import adler
from observations.rdata.angell import angell
from observations.rdata.us_public_school import us_public_school
from observations.rdata.baumann import baumann
from observations.rdata.bfox import bfox
from observations.rdata.blackmore import blackmore
from observations.rdata.burt import burt
from observations.rdata.can_pop import can_pop
from observations.rdata.chile import chile
from observations.rdata.chirot import chirot
from observations.rdata.cowles import cowles
from observations.rdata.davis import davis
from observations.rdata.davis_thin import davis_thin
from observations.rdata.depredations import depredations
from observations.rdata.duncan import duncan
from observations.rdata.ericksen import ericksen
from observations.rdata.florida import florida
from observations.rdata.freedman import freedman
from observations.rdata.friendly import friendly
from observations.rdata.ginzberg import ginzberg
from observations.rdata.greene import greene
from observations.rdata.guyer import guyer
from observations.rdata.hartnagel import hartnagel
from observations.rdata.highway1 import highway1
from observations.rdata.kostecki_dillon import kostecki_dillon
from observations.rdata.leinhardt import leinhardt
from observations.rdata.lo_bd import lo_bd
from observations.rdata.mandel import mandel
from observations.rdata.migration import migration
from observations.rdata.moore import moore
from observations.rdata.mroz import mroz
from observations.rdata.o_brien_kaiser import o_brien_kaiser
from observations.rdata.ornstein import ornstein
from observations.rdata.pottery import pottery
from observations.rdata.prestige import prestige
from observations.rdata.quartet import quartet
from observations.rdata.robey import robey
from observations.rdata.slid import slid
from observations.rdata.sahlins import sahlins
from observations.rdata.salaries import salaries
from observations.rdata.soils import soils
from observations.rdata.states import states
from observations.rdata.transact import transact
from observations.rdata.un_gdp_infant_mortality import un_gdp_infant_mortality
from observations.rdata.us_pop import us_pop
from observations.rdata.vocab import vocab
from observations.rdata.weight_loss import weight_loss
from observations.rdata.womenlf import womenlf
from observations.rdata.wong import wong
from observations.rdata.wool1 import wool1
from observations.rdata.agriculture import agriculture
from observations.rdata.animals import animals
from observations.rdata.chor_sub import chor_sub
from observations.rdata.flower import flower
from observations.rdata.plant_traits import plant_traits
from observations.rdata.pluton import pluton
from observations.rdata.ruspini import ruspini
from observations.rdata.votes_repub import votes_repub
from observations.rdata.xclara import xclara
from observations.rdata.affairs import affairs
from observations.rdata.azcabgptca import azcabgptca
from observations.rdata.azdrg112 import azdrg112
from observations.rdata.azpro import azpro
from observations.rdata.azprocedure import azprocedure
from observations.rdata.badhealth import badhealth
from observations.rdata.fasttrakg import fasttrakg
from observations.rdata.fishing import fishing
from observations.rdata.lbw import lbw
from observations.rdata.lbwgrp import lbwgrp
from observations.rdata.loomis import loomis
from observations.rdata.mdvis import mdvis
from observations.rdata.medpar import medpar
from observations.rdata.nuts import nuts
from observations.rdata.rwm import rwm
from observations.rdata.rwm1984 import rwm1984
from observations.rdata.rwm5yr import rwm5yr
from observations.rdata.smoking import smoking
from observations.rdata.titanicgrp import titanicgrp
from observations.rdata.accident import accident
from observations.rdata.airline import airline
from observations.rdata.airq import airq
from observations.rdata.benefits import benefits
from observations.rdata.bids import bids
from observations.rdata.budget_food import budget_food
from observations.rdata.budget_italy import budget_italy
from observations.rdata.budget_uk import budget_uk
from observations.rdata.bwages import bwages
from observations.rdata.cp_sch3 import cp_sch3
from observations.rdata.cran_packages import cran_packages
from observations.rdata.capm import capm
from observations.rdata.car import car
from observations.rdata.caschool import caschool
from observations.rdata.catsup import catsup
from observations.rdata.cigar import cigar
from observations.rdata.cigarette import cigarette
from observations.rdata.clothing import clothing
from observations.rdata.computers import computers
from observations.rdata.cracker import cracker
from observations.rdata.crime import crime
from observations.rdata.dm import dm
from observations.rdata.diamond import diamond
from observations.rdata.doctor import doctor
from observations.rdata.doctor_aus import doctor_aus
from observations.rdata.doctor_contacts import doctor_contacts
from observations.rdata.earnings import earnings
from observations.rdata.electricity import electricity
from observations.rdata.fair import fair
from observations.rdata.fatality import fatality
from observations.rdata.fishing1 import fishing1
from observations.rdata.forward import forward
from observations.rdata.friend_foe import friend_foe
from observations.rdata.garch import garch
from observations.rdata.gasoline import gasoline
from observations.rdata.griliches import griliches
from observations.rdata.grunfeld import grunfeld
from observations.rdata.hc_choice_california import hc_choice_california
from observations.rdata.hhs_cyber_security_breaches import hhs_cyber_security_breaches
from observations.rdata.hi_hours_worked import hi_hours_worked
from observations.rdata.hdma import hdma
from observations.rdata.heating import heating
from observations.rdata.hedonic import hedonic
from observations.rdata.hmda import hmda
from observations.rdata.housing import housing
from observations.rdata.icecream import icecream
from observations.rdata.journals import journals
from observations.rdata.kakadu import kakadu
from observations.rdata.ketchup import ketchup
from observations.rdata.klein import klein
from observations.rdata.labor_supply import labor_supply
from observations.rdata.labour import labour
from observations.rdata.mcas import mcas
from observations.rdata.males import males
from observations.rdata.mathlevel import mathlevel
from observations.rdata.med_exp import med_exp
from observations.rdata.metal import metal
from observations.rdata.mode import mode
from observations.rdata.mode_choice import mode_choice
from observations.rdata.mofa import mofa
from observations.rdata.mroz1 import mroz1
from observations.rdata.mun_exp import mun_exp
from observations.rdata.natural_park import natural_park
from observations.rdata.nerlove import nerlove
from observations.rdata.ofp import ofp
from observations.rdata.oil import oil
from observations.rdata.psid import psid
from observations.rdata.participation import participation
from observations.rdata.patents_hgh import patents_hgh
from observations.rdata.patents_rd import patents_rd
from observations.rdata.pound import pound
from observations.rdata.produc import produc
from observations.rdata.ret_school import ret_school
from observations.rdata.sp500 import sp500
from observations.rdata.schooling import schooling
from observations.rdata.somerville import somerville
from observations.rdata.star import star
from observations.rdata.strike import strike
from observations.rdata.strike_dur import strike_dur
from observations.rdata.strike_nb import strike_nb
from observations.rdata.tobacco import tobacco
from observations.rdata.train import train
from observations.rdata.transp_eq import transp_eq
from observations.rdata.treatment import treatment
from observations.rdata.tuna1 import tuna1
from observations.rdata.us_finance_industry import us_finance_industry
from observations.rdata.us_gdp_presidents import us_gdp_presidents
from observations.rdata.us_classified_documents import us_classified_documents
from observations.rdata.us_state_abbreviations import us_state_abbreviations
from observations.rdata.us_tax_words import us_tax_words
from observations.rdata.unemp_dur import unemp_dur
from observations.rdata.unemployment import unemployment
from observations.rdata.university import university
from observations.rdata.vietnam_h import vietnam_h
from observations.rdata.vietnam_i import vietnam_i
from observations.rdata.wages import wages
from observations.rdata.wages1 import wages1
from observations.rdata.workinghours import workinghours
from observations.rdata.yen import yen
from observations.rdata.yogurt import yogurt
from observations.rdata.banking_crises import banking_crises
from observations.rdata.breaches import breaches
from observations.rdata.incidents_by_country_yr import incidents_by_country_yr
from observations.rdata.income_inequality import income_inequality
from observations.rdata.nkill_by_country_yr import nkill_by_country_yr
from observations.rdata.non_english_names import non_english_names
from observations.rdata.political_knowledge import political_knowledge
from observations.rdata.terrorism import terrorism
from observations.rdata.parkinsons import parkinsons
from observations.rdata.aldh2 import aldh2
from observations.rdata.apoeapoc import apoeapoc
from observations.rdata.cf import cf
from observations.rdata.crohn import crohn
from observations.rdata.fa import fa
from observations.rdata.fsnps import fsnps
from observations.rdata.hla import hla
from observations.rdata.hr1420 import hr1420
from observations.rdata.l51 import l51
from observations.rdata.lukas import lukas
from observations.rdata.mao import mao
from observations.rdata.meyer import meyer
from observations.rdata.mfblong import mfblong
from observations.rdata.mhtdata import mhtdata
from observations.rdata.nep499 import nep499
from observations.rdata.luv_colours import luv_colours
from observations.rdata.arbuthnot import arbuthnot
from observations.rdata.armada import armada
from observations.rdata.bowley import bowley
from observations.rdata.cavendish import cavendish
from observations.rdata.chest_sizes import chest_sizes
from observations.rdata.cholera import cholera
from observations.rdata.cushny_peebles import cushny_peebles
from observations.rdata.cushny_peebles_n import cushny_peebles_n
from observations.rdata.dactyl import dactyl
from observations.rdata.drinks_wages import drinks_wages
from observations.rdata.fingerprints import fingerprints
from observations.rdata.galton import galton
from observations.rdata.galton_families import galton_families
from observations.rdata.guerry import guerry
from observations.rdata.halley_life_table import halley_life_table
from observations.rdata.jevons import jevons
from observations.rdata.langren_all import langren_all
from observations.rdata.langren1644 import langren1644
from observations.rdata.macdonell import macdonell
from observations.rdata.macdonell_df import macdonell_df
from observations.rdata.michelson import michelson
from observations.rdata.michelson_sets import michelson_sets
from observations.rdata.minard_cities import minard_cities
from observations.rdata.minard_temp import minard_temp
from observations.rdata.minard_troops import minard_troops
from observations.rdata.nightingale import nightingale
from observations.rdata.old_maps import old_maps
from observations.rdata.pearson_lee import pearson_lee
from observations.rdata.polio_trials import polio_trials
from observations.rdata.prostitutes import prostitutes
from observations.rdata.pyx import pyx
from observations.rdata.quarrels import quarrels
from observations.rdata.snow_dates import snow_dates
from observations.rdata.snow_deaths import snow_deaths
from observations.rdata.snow_deaths2 import snow_deaths2
from observations.rdata.snow_pumps import snow_pumps
from observations.rdata.snow_streets import snow_streets
from observations.rdata.wheat import wheat
from observations.rdata.wheat_monarchs import wheat_monarchs
from observations.rdata.yeast import yeast
from observations.rdata.yeast_d_mat import yeast_d_mat
from observations.rdata.zea_mays import zea_mays
from observations.rdata.barley import barley
from observations.rdata.environmental import environmental
from observations.rdata.ethanol import ethanol
from observations.rdata.melanoma import melanoma
from observations.rdata.singer import singer
from observations.rdata.aids2 import aids2
from observations.rdata.animals1 import animals1
from observations.rdata.boston import boston
from observations.rdata.cars93 import cars93
from observations.rdata.cushings import cushings
from observations.rdata.ddt_kale import ddt_kale
from observations.rdata.gag_urine import gag_urine
from observations.rdata.insurance import insurance
from observations.rdata.melanoma1 import melanoma1
from observations.rdata.ome_children import ome_children
from observations.rdata.pima_te import pima_te
from observations.rdata.pima_tr import pima_tr
from observations.rdata.pima_tr2 import pima_tr2
from observations.rdata.rabbit import rabbit
from observations.rdata.rubber import rubber
from observations.rdata.sitka import sitka
from observations.rdata.sitka89 import sitka89
from observations.rdata.skye import skye
from observations.rdata.traffic import traffic
from observations.rdata.us_cereal import us_cereal
from observations.rdata.us_crime import us_crime
from observations.rdata.va_lung_cancer import va_lung_cancer
from observations.rdata.abbey import abbey
from observations.rdata.accdeaths import accdeaths
from observations.rdata.anorexia import anorexia
from observations.rdata.bacteria import bacteria
from observations.rdata.beav1 import beav1
from observations.rdata.beav2 import beav2
from observations.rdata.biopsy import biopsy
from observations.rdata.birthwt import birthwt
from observations.rdata.cabbages import cabbages
from observations.rdata.caith import caith
from observations.rdata.cats import cats
from observations.rdata.cement import cement
from observations.rdata.chem import chem
from observations.rdata.coop import coop
from observations.rdata.cpus import cpus
from observations.rdata.crabs import crabs
from observations.rdata.deaths import deaths
from observations.rdata.drivers import drivers
from observations.rdata.eagles import eagles
from observations.rdata.epil import epil
from observations.rdata.farms import farms
from observations.rdata.fgl import fgl
from observations.rdata.forbes import forbes
from observations.rdata.galaxies import galaxies
from observations.rdata.gehan import gehan
from observations.rdata.genotype import genotype
from observations.rdata.geyser import geyser
from observations.rdata.gilgais import gilgais
from observations.rdata.housing1 import housing1
from observations.rdata.immer import immer
from observations.rdata.leuk import leuk
from observations.rdata.mammals import mammals
from observations.rdata.mcycle import mcycle
from observations.rdata.menarche import menarche
from observations.rdata.michelson1 import michelson1
from observations.rdata.minn38 import minn38
from observations.rdata.motors import motors
from observations.rdata.muscle import muscle
from observations.rdata.newcomb import newcomb
from observations.rdata.nlschools import nlschools
from observations.rdata.npr1 import npr1
from observations.rdata.oats import oats
from observations.rdata.painters import painters
from observations.rdata.petrol import petrol
from observations.rdata.quine import quine
from observations.rdata.road import road
from observations.rdata.rotifer import rotifer
from observations.rdata.ships import ships
from observations.rdata.shrimp import shrimp
from observations.rdata.shuttle import shuttle
from observations.rdata.snails import snails
from observations.rdata.steam import steam
from observations.rdata.stormer import stormer
from observations.rdata.survey import survey
from observations.rdata.synth_te import synth_te
from observations.rdata.synth_tr import synth_tr
from observations.rdata.topo import topo
from observations.rdata.waders import waders
from observations.rdata.whiteside import whiteside
from observations.rdata.wtloss import wtloss
from observations.rdata.empl_uk import empl_uk
from observations.rdata.grunfeld1 import grunfeld1
from observations.rdata.males1 import males1
from observations.rdata.parity import parity
from observations.rdata.rice_farms import rice_farms
from observations.rdata.snmesp import snmesp
from observations.rdata.sum_hes import sum_hes
from observations.rdata.baseball import baseball
from observations.rdata.australian_election_polling import australian_election_polling
from observations.rdata.australian_elections import australian_elections
from observations.rdata.efron_morris import efron_morris
from observations.rdata.rock_the_vote import rock_the_vote
from observations.rdata.uk_house_of_commons import uk_house_of_commons
from observations.rdata.absentee import absentee
from observations.rdata.admit import admit
from observations.rdata.bio_chemists import bio_chemists
from observations.rdata.ca2006 import ca2006
from observations.rdata.iraq_vote import iraq_vote
from observations.rdata.political_information import political_information
from observations.rdata.presidential_elections import presidential_elections
from observations.rdata.prussian import prussian
from observations.rdata.union_density import union_density
from observations.rdata.vote92 import vote92
from observations.rdata.french_fries import french_fries
from observations.rdata.tips import tips
from observations.rdata.car_test_frame import car_test_frame
from observations.rdata.car90 import car90
from observations.rdata.cu_summary import cu_summary
from observations.rdata.kyphosis import kyphosis
from observations.rdata.solder import solder
from observations.rdata.stagec import stagec
from observations.rdata.public_schools import public_schools
from observations.rdata.bollen import bollen
from observations.rdata.cnes import cnes
from observations.rdata.klein1 import klein1
from observations.rdata.mental_tests import mental_tests
from observations.rdata.bladder import bladder
from observations.rdata.cancer import cancer
from observations.rdata.cgd import cgd
from observations.rdata.colon import colon
from observations.rdata.flchain import flchain
from observations.rdata.genfan import genfan
from observations.rdata.kidney import kidney
from observations.rdata.leukemia import leukemia
from observations.rdata.logan import logan
from observations.rdata.lung import lung
from observations.rdata.mgus import mgus
from observations.rdata.mgus2 import mgus2
from observations.rdata.myeloid import myeloid
from observations.rdata.nwtco import nwtco
from observations.rdata.ovarian import ovarian
from observations.rdata.pbc import pbc
from observations.rdata.rats import rats
from observations.rdata.retinopathy import retinopathy
from observations.rdata.rh_dnase import rh_dnase
from observations.rdata.stanford2 import stanford2
from observations.rdata.tobin import tobin
from observations.rdata.transplant import transplant
from observations.rdata.veteran import veteran
from observations.rdata.arthritis import arthritis
from observations.rdata.baseball1 import baseball1
from observations.rdata.broken_marriage import broken_marriage
from observations.rdata.bundesliga import bundesliga
from observations.rdata.bundestag2005 import bundestag2005
from observations.rdata.butterfly import butterfly
from observations.rdata.coal_miners import coal_miners
from observations.rdata.danish_welfare import danish_welfare
from observations.rdata.employment import employment
from observations.rdata.federalist import federalist
from observations.rdata.hitters import hitters
from observations.rdata.horse_kicks import horse_kicks
from observations.rdata.hospital import hospital
from observations.rdata.job_satisfaction import job_satisfaction
from observations.rdata.joint_sports import joint_sports
from observations.rdata.lifeboats import lifeboats
from observations.rdata.non_response import non_response
from observations.rdata.ovary_cancer import ovary_cancer
from observations.rdata.pre_sex import pre_sex
from observations.rdata.punishment import punishment
from observations.rdata.rep_vict import rep_vict
from observations.rdata.saxony import saxony
from observations.rdata.sexual_fun import sexual_fun
from observations.rdata.space_shuttle import space_shuttle
from observations.rdata.suicide import suicide
from observations.rdata.trucks import trucks
from observations.rdata.uk_soccer import uk_soccer
from observations.rdata.visual_acuity import visual_acuity
from observations.rdata.von_bort import von_bort
from observations.rdata.weldon_dice import weldon_dice
from observations.rdata.women_queue import women_queue
from observations.rdata.p_erisk import p_erisk
from observations.rdata.supreme_court import supreme_court
from observations.rdata.weimar import weimar
from observations.rdata.approval import approval
from observations.rdata.bivariate import bivariate
from observations.rdata.coalition import coalition
from observations.rdata.coalition2 import coalition2
from observations.rdata.eidat import eidat
from observations.rdata.free1 import free1
from observations.rdata.free2 import free2
from observations.rdata.friendship import friendship
from observations.rdata.grunfeld2 import grunfeld2
from observations.rdata.hoff import hoff
from observations.rdata.homerun import homerun
from observations.rdata.immi1 import immi1
from observations.rdata.immi2 import immi2
from observations.rdata.immi3 import immi3
from observations.rdata.immi4 import immi4
from observations.rdata.immi5 import immi5
from observations.rdata.immigration import immigration
from observations.rdata.klein2 import klein2
from observations.rdata.kmenta2 import kmenta2
from observations.rdata.macro import macro
from observations.rdata.mexico import mexico
from observations.rdata.mid import mid
from observations.rdata.newpainters import newpainters
from observations.rdata.sanction import sanction
from observations.rdata.seatshare import seatshare
from observations.rdata.sna_ex import sna_ex
from observations.rdata.turnout import turnout
from observations.rdata.voteincome import voteincome
from observations.rdata.bcg_vaccine import bcg_vaccine
from observations.rdata.bthe_b import bthe_b
from observations.rdata.cygob1 import cygob1
from observations.rdata.forbes2000 import forbes2000
from observations.rdata.ghq import ghq
from observations.rdata.lanza import lanza
from observations.rdata.agefat import agefat
from observations.rdata.aspirin import aspirin
from observations.rdata.birthdeathrates import birthdeathrates
from observations.rdata.bladdercancer import bladdercancer
from observations.rdata.clouds import clouds
from observations.rdata.foster import foster
from observations.rdata.heptathlon import heptathlon
from observations.rdata.mastectomy import mastectomy
from observations.rdata.meteo import meteo
from observations.rdata.orallesions import orallesions
from observations.rdata.phosphate import phosphate
from observations.rdata.pistonrings import pistonrings
from observations.rdata.planets import planets
from observations.rdata.plasma import plasma
from observations.rdata.polyps import polyps
from observations.rdata.polyps3 import polyps3
from observations.rdata.pottery1 import pottery1
from observations.rdata.rearrests import rearrests
from observations.rdata.respiratory import respiratory
from observations.rdata.roomwidth import roomwidth
from observations.rdata.schizophrenia import schizophrenia
from observations.rdata.schizophrenia2 import schizophrenia2
from observations.rdata.schooldays import schooldays
from observations.rdata.skulls import skulls
from observations.rdata.students import students
from observations.rdata.suicides import suicides
from observations.rdata.toothpaste import toothpaste
from observations.rdata.voting import voting
from observations.rdata.water import water
from observations.rdata.watervoles import watervoles
from observations.rdata.waves import waves
from observations.rdata.weightgain import weightgain
from observations.rdata.womensrole import womensrole
from observations.rdata.bechtoldt import bechtoldt
from observations.rdata.bechtoldt_1 import bechtoldt_1
from observations.rdata.bechtoldt_2 import bechtoldt_2
from observations.rdata.dwyer import dwyer
from observations.rdata.gleser import gleser
from observations.rdata.gorsuch import gorsuch
from observations.rdata.harman_5 import harman_5
from observations.rdata.harman_8 import harman_8
from observations.rdata.harman_political import harman_political
from observations.rdata.holzinger import holzinger
from observations.rdata.holzinger_9 import holzinger_9
from observations.rdata.reise import reise
from observations.rdata.schmid import schmid
from observations.rdata.schutz import schutz
from observations.rdata.thurstone import thurstone
from observations.rdata.thurstone_33 import thurstone_33
from observations.rdata.tucker import tucker
from observations.rdata.ability import ability
from observations.rdata.affect import affect
from observations.rdata.bfi import bfi
from observations.rdata.bfi_dictionary import bfi_dictionary
from observations.rdata.blot import blot
from observations.rdata.burt1 import burt1
from observations.rdata.cattell import cattell
from observations.rdata.cities1 import cities1
from observations.rdata.cubits import cubits
from observations.rdata.epi import epi
from observations.rdata.epi_bfi import epi_bfi
from observations.rdata.epi_dictionary import epi_dictionary
from observations.rdata.galton1 import galton1
from observations.rdata.heights import heights
from observations.rdata.income import income
from observations.rdata.iqitems import iqitems
from observations.rdata.msq import msq
from observations.rdata.neo import neo
from observations.rdata.peas import peas
from observations.rdata.sat_act import sat_act
from observations.rdata.within_between import within_between
from observations.rdata.bosco import bosco
from observations.rdata.cobar_ore import cobar_ore
from observations.rdata.mammals1 import mammals1
from observations.rdata.barro import barro
from observations.rdata.engel import engel
from observations.rdata.gasprice import gasprice
from observations.rdata.uis import uis
from observations.rdata.dietox import dietox
from observations.rdata.koch import koch
from observations.rdata.ohio import ohio
from observations.rdata.respdis import respdis
from observations.rdata.seizure import seizure
from observations.rdata.spruce import spruce
from observations.rdata.liver import liver
from observations.rdata.nidd import nidd
from observations.rdata.portpirie import portpirie
from observations.rdata.rain import rain
from observations.rdata.summer import summer
from observations.rdata.wavesurge import wavesurge
from observations.rdata.winter import winter
from observations.rdata.arthritis1 import arthritis1
from observations.rdata.bmw import bmw
from observations.rdata.danish import danish
from observations.rdata.nidd_annual import nidd_annual
from observations.rdata.nidd_thresh import nidd_thresh
from observations.rdata.siemens import siemens
from observations.rdata.sp_raw import sp_raw
from observations.rdata.spto87 import spto87
from observations.rdata.arabidopsis import arabidopsis
from observations.rdata.dyestuff import dyestuff
from observations.rdata.dyestuff2 import dyestuff2
from observations.rdata.pastes import pastes
from observations.rdata.penicillin import penicillin
from observations.rdata.verb_agg import verb_agg
from observations.rdata.cake import cake
from observations.rdata.cbpp import cbpp
from observations.rdata.grouseticks import grouseticks
from observations.rdata.sleepstudy import sleepstudy
from observations.rdata.alcohol1 import alcohol1
from observations.rdata.birthdays import birthdays
from observations.rdata.births import births
from observations.rdata.births78 import births78
from observations.rdata.cps_85 import cps_85
from observations.rdata.cooling_water import cooling_water
from observations.rdata.countries import countries
from observations.rdata.dimes import dimes
from observations.rdata.galton2 import galton2
from observations.rdata.gestation import gestation
from observations.rdata.goose_permits import goose_permits
from observations.rdata.help_full import help_full
from observations.rdata.help_miss import help_miss
from observations.rdata.help_rct import help_rct
from observations.rdata.heat_x import heat_x
from observations.rdata.kids_feet import kids_feet
from observations.rdata.marriage import marriage
from observations.rdata.mites import mites
from observations.rdata.rail_trail import rail_trail
from observations.rdata.riders import riders
from observations.rdata.sat_state import sat_state
from observations.rdata.saratoga_houses import saratoga_houses
from observations.rdata.snow_gr import snow_gr
from observations.rdata.swim_records import swim_records
from observations.rdata.ten_mile_race import ten_mile_race
from observations.rdata.utilities import utilities
from observations.rdata.utilities2 import utilities2
from observations.rdata.whickham import whickham
from observations.rdata.auto import auto
from observations.rdata.caravan import caravan
from observations.rdata.carseats import carseats
from observations.rdata.college import college
from observations.rdata.default import default
from observations.rdata.oj import oj
from observations.rdata.portfolio import portfolio
from observations.rdata.smarket import smarket
from observations.rdata.wage import wage
from observations.rdata.weekly import weekly
from observations.rdata.alfalfa import alfalfa
from observations.rdata.archery_data import archery_data
from observations.rdata.auto_pollution import auto_pollution
from observations.rdata.backpack import backpack
from observations.rdata.baseball_times import baseball_times
from observations.rdata.bee_stings import bee_stings
from observations.rdata.bird_nest import bird_nest
from observations.rdata.blood1 import blood1
from observations.rdata.blue_jays import blue_jays
from observations.rdata.british_unions import british_unions
from observations.rdata.cafe import cafe
from observations.rdata.calcium_bp import calcium_bp
from observations.rdata.cancer_survival import cancer_survival
from observations.rdata.caterpillars import caterpillars
from observations.rdata.cereal import cereal
from observations.rdata.chemo_thc import chemo_thc
from observations.rdata.child_speaks import child_speaks
from observations.rdata.cloud_seeding import cloud_seeding
from observations.rdata.cloud_seeding2 import cloud_seeding2
from observations.rdata.cracker_fiber import cracker_fiber
from observations.rdata.cuckoo import cuckoo
from observations.rdata.day1_survey import day1_survey
from observations.rdata.diamonds import diamonds
from observations.rdata.diamonds2 import diamonds2
from observations.rdata.election08 import election08
from observations.rdata.ethanol1 import ethanol1
from observations.rdata.fgb_y_distance import fgb_y_distance
from observations.rdata.fantasy_baseball import fantasy_baseball
from observations.rdata.fertility import fertility
from observations.rdata.film import film
from observations.rdata.final_four_izzo import final_four_izzo
from observations.rdata.final_four_long import final_four_long
from observations.rdata.final_four_short import final_four_short
from observations.rdata.fingers import fingers
from observations.rdata.first_year_gpa import first_year_gpa
from observations.rdata.fish_eggs import fish_eggs
from observations.rdata.flight_response import flight_response
from observations.rdata.fluorescence import fluorescence
from observations.rdata.fruit_flies import fruit_flies
from observations.rdata.goldenrod import goldenrod
from observations.rdata.grocery import grocery
from observations.rdata.gunnels import gunnels
from observations.rdata.hawk_tail import hawk_tail
from observations.rdata.hawk_tail2 import hawk_tail2
from observations.rdata.hawks import hawks
from observations.rdata.hearing_test import hearing_test
from observations.rdata.high_peaks import high_peaks
from observations.rdata.hoops import hoops
from observations.rdata.horse_prices import horse_prices
from observations.rdata.houses import houses
from observations.rdata.icu import icu
from observations.rdata.infant_mortality import infant_mortality
from observations.rdata.insurance_vote import insurance_vote
from observations.rdata.jurors import jurors
from observations.rdata.kids198 import kids198
from observations.rdata.leaf_hoppers import leaf_hoppers
from observations.rdata.leukemia1 import leukemia1
from observations.rdata.long_jump_olympics import long_jump_olympics
from observations.rdata.lost_letter import lost_letter
from observations.rdata.mlb_2007_standings import mlb_2007_standings
from observations.rdata.marathon import marathon
from observations.rdata.markets import markets
from observations.rdata.math_enrollment import math_enrollment
from observations.rdata.math_placement import math_placement
from observations.rdata.med_gpa import med_gpa
from observations.rdata.mental_health import mental_health
from observations.rdata.metabolic_rate import metabolic_rate
from observations.rdata.metro_health83 import metro_health83
from observations.rdata.milgram import milgram
from observations.rdata.moth_eggs import moth_eggs
from observations.rdata.n_cbirths import n_cbirths
from observations.rdata.n_f_l2007_standings import n_f_l2007_standings
from observations.rdata.nursing import nursing
from observations.rdata.olives import olives
from observations.rdata.orings1 import orings1
from observations.rdata.overdrawn import overdrawn
from observations.rdata.palm_beach import palm_beach
from observations.rdata.pedometer import pedometer
from observations.rdata.perch import perch
from observations.rdata.pig_feed import pig_feed
from observations.rdata.pines import pines
from observations.rdata.political import political
from observations.rdata.pollster08 import pollster08
from observations.rdata.popcorn import popcorn
from observations.rdata.porsche_jaguar import porsche_jaguar
from observations.rdata.porsche_price import porsche_price
from observations.rdata.pulse import pulse
from observations.rdata.putts1 import putts1
from observations.rdata.putts2 import putts2
from observations.rdata.religion_gdp import religion_gdp
from observations.rdata.retirement import retirement
from observations.rdata.river_elements import river_elements
from observations.rdata.river_iron import river_iron
from observations.rdata.sat_gpa import sat_gpa
from observations.rdata.sample_fg import sample_fg
from observations.rdata.sandwich_ants import sandwich_ants
from observations.rdata.sea_slugs import sea_slugs
from observations.rdata.sparrows import sparrows
from observations.rdata.species_area import species_area
from observations.rdata.speed import speed
from observations.rdata.swahili import swahili
from observations.rdata.tms import tms
from observations.rdata.text_prices import text_prices
from observations.rdata.three_cars import three_cars
from observations.rdata.tip_joke import tip_joke
from observations.rdata.tomlinson_rush import tomlinson_rush
from observations.rdata.twins_lungs import twins_lungs
from observations.rdata.us_stamps import us_stamps
from observations.rdata.volts import volts
from observations.rdata.walking_babies import walking_babies
from observations.rdata.weight_loss_incentive import weight_loss_incentive
from observations.rdata.weight_loss_incentive4 import weight_loss_incentive4
from observations.rdata.weight_loss_incentive7 import weight_loss_incentive7
from observations.rdata.word_memory import word_memory
from observations.rdata.youth_risk2007 import youth_risk2007
from observations.rdata.youth_risk2009 import youth_risk2009
from observations.rdata.indian_irish import indian_irish
from observations.rdata.mendel_abc import mendel_abc
from observations.rdata.chain import chain
from observations.rdata.nlsy_v import nlsy_v
from observations.rdata.ced_data import ced_data
from observations.rdata.boundsdata import boundsdata
from observations.rdata.framing import framing
from observations.rdata.school import school
from observations.rdata.student import student
from observations.rdata.admnrev import admnrev
from observations.rdata.airfare import airfare
from observations.rdata.apple import apple
from observations.rdata.athlet1 import athlet1
from observations.rdata.athlet2 import athlet2
from observations.rdata.attend import attend
from observations.rdata.audit import audit
from observations.rdata.barium import barium
from observations.rdata.beauty import beauty
from observations.rdata.benefits1 import benefits1
from observations.rdata.beveridge import beveridge
from observations.rdata.big9salary import big9salary
from observations.rdata.bwght import bwght
from observations.rdata.bwght2 import bwght2
from observations.rdata.campus import campus
from observations.rdata.card import card
from observations.rdata.ceosal1 import ceosal1
from observations.rdata.ceosal2 import ceosal2
from observations.rdata.charity import charity
from observations.rdata.consump import consump
from observations.rdata.corn import corn
from observations.rdata.cps78_85 import cps78_85
from observations.rdata.cps91 import cps91
from observations.rdata.crime1 import crime1
from observations.rdata.crime2 import crime2
from observations.rdata.crime3 import crime3
from observations.rdata.crime4 import crime4
from observations.rdata.discrim import discrim
from observations.rdata.driving import driving
from observations.rdata.earns import earns
from observations.rdata.elem94_95 import elem94_95
from observations.rdata.engin import engin
from observations.rdata.expendshares import expendshares
from observations.rdata.ezanders import ezanders
from observations.rdata.ezunem import ezunem
from observations.rdata.fair1 import fair1
from observations.rdata.fertil1 import fertil1
from observations.rdata.fertil2 import fertil2
from observations.rdata.fertil3 import fertil3
from observations.rdata.fish import fish
from observations.rdata.fringe import fringe
from observations.rdata.gpa1 import gpa1
from observations.rdata.gpa2 import gpa2
from observations.rdata.gpa3 import gpa3
from observations.rdata.happiness import happiness
from observations.rdata.hprice1 import hprice1
from observations.rdata.hprice2 import hprice2
from observations.rdata.hprice3 import hprice3
from observations.rdata.hseinv import hseinv
from observations.rdata.htv import htv
from observations.rdata.infmrt import infmrt
from observations.rdata.injury import injury
from observations.rdata.intdef import intdef
from observations.rdata.intqrt import intqrt
from observations.rdata.inven import inven
from observations.rdata.jtrain import jtrain
from observations.rdata.jtrain2 import jtrain2
from observations.rdata.jtrain3 import jtrain3
from observations.rdata.kielmc import kielmc
from observations.rdata.lawsch85 import lawsch85
from observations.rdata.loanapp import loanapp
from observations.rdata.lowbrth import lowbrth
from observations.rdata.mathpnl import mathpnl
from observations.rdata.meap00_01 import meap00_01
from observations.rdata.meap01 import meap01
from observations.rdata.meap93 import meap93
from observations.rdata.minwage import minwage
from observations.rdata.mlb1 import mlb1
from observations.rdata.mroz2 import mroz2
from observations.rdata.murder import murder
from observations.rdata.nbasal import nbasal
from observations.rdata.nyse import nyse
from observations.rdata.okun import okun
from observations.rdata.openness import openness
from observations.rdata.phillips import phillips
from observations.rdata.pntsprd import pntsprd
from observations.rdata.prison import prison
from observations.rdata.prminwge import prminwge
from observations.rdata.rdchem import rdchem
from observations.rdata.rdtelec import rdtelec
from observations.rdata.recid import recid
from observations.rdata.rental import rental
from observations.rdata.company_return import company_return
from observations.rdata.saving import saving
from observations.rdata.sleep75 import sleep75
from observations.rdata.slp75_81 import slp75_81
from observations.rdata.smoke import smoke
from observations.rdata.traffic1 import traffic1
from observations.rdata.traffic2 import traffic2
from observations.rdata.twoyear import twoyear
from observations.rdata.volat import volat
from observations.rdata.vote1 import vote1
from observations.rdata.vote2 import vote2
from observations.rdata.voucher import voucher
from observations.rdata.wage1 import wage1
from observations.rdata.wage2 import wage2
from observations.rdata.wagepan import wagepan
from observations.rdata.wageprc import wageprc
from observations.rdata.wine import wine


def remove_undocumented(module_name, allowed_exception_list=None):
  """Removes symbols in a module that are not referenced by a docstring.

  Args:
    module_name: the name of the module (usually `__name__`).
    allowed_exception_list: a list of names that should not be removed.

  Returns:
    None
  """
  import sys as _sys
  current_symbols = set(dir(_sys.modules[module_name]))
  should_have = allowed_exception_list or []
  extra_symbols = current_symbols - set(should_have)
  target_module = _sys.modules[module_name]
  for extra_symbol in extra_symbols:
    # Skip over __file__, etc. Also preserves internal symbols.
    if extra_symbol.startswith('_'):
      continue
    fully_qualified_name = module_name + '.' + extra_symbol
    delattr(target_module, extra_symbol)


# Export modules and constants.
_allowed_symbols = [
      'air_passengers',
    'bj_sales',
    'bod',
    'co2',
    'formaldehyde',
    'hair_eye_color',
    'insect_sprays',
    'johnson_johnson',
    'lake_huron',
    'life_cycle_savings',
    'nile',
    'orchard_sprays',
    'plant_growth',
    'puromycin',
    'titanic',
    'tooth_growth',
    'ucb_admissions',
    'uk_driver_deaths',
    'uk_gas',
    'us_acc_deaths',
    'us_arrests',
    'us_judge_ratings',
    'us_personal_expenditure',
    'va_deaths',
    'www_usage',
    'world_phones',
    'airmiles',
    'airquality',
    'anscombe',
    'attenu',
    'attitude',
    'austres',
    'cars',
    'chickwts',
    'co2_1',
    'crimtab',
    'discoveries',
    'esoph',
    'euro',
    'faithful',
    'freeny',
    'infert',
    'iris',
    'islands',
    'lh',
    'longley',
    'lynx',
    'morley',
    'mtcars',
    'nhtemp',
    'nottem',
    'npk',
    'occupational_status',
    'precip',
    'presidents',
    'pressure',
    'quakes',
    'randu',
    'rivers',
    'rock',
    'sleep',
    'stackloss',
    'sunspot_month',
    'sunspot_year',
    'sunspots',
    'swiss',
    'treering',
    'trees',
    'uspop',
    'volcano',
    'warpbreaks',
    'women',
    'acme',
    'aids',
    'aircondit',
    'aircondit7',
    'amis',
    'aml',
    'bigcity',
    'brambles',
    'breslow',
    'calcium',
    'cane',
    'capability',
    'cats_m',
    'cav',
    'cd4',
    'channing',
    'city',
    'claridge',
    'cloth',
    'co_transfer',
    'coal',
    'darwin',
    'dogs',
    'downs_bc',
    'ducks',
    'fir',
    'frets',
    'grav',
    'gravity',
    'hirose',
    'islay',
    'manaus',
    'melanoma',
    'motor',
    'neuro',
    'nitrofen',
    'nodal',
    'nuclear',
    'paulsen',
    'poisons',
    'polar',
    'remission',
    'salinity',
    'survival',
    'tau',
    'tuna',
    'urine',
    'wool',
    'acf1',
    'cars93_summary',
    'lottario',
    'manitoba_lakes',
    'sp500_w90',
    'sp500_close',
    'ais',
    'allbacks',
    'anesthetic',
    'ant111b',
    'antigua',
    'appletaste',
    'aulatlong',
    'austpop',
    'biomass',
    'bomregions',
    'bomregions2011',
    'bomregions2012',
    'bomsoi',
    'bomsoi2001',
    'carprice',
    'cerealsugar',
    'cfseal',
    'cities',
    'codling',
    'cottonworkers',
    'cps1',
    'cps2',
    'cps3',
    'cricketer',
    'cuckoohosts',
    'cuckoos',
    'dengue',
    'dewpoint',
    'droughts',
    'edc_co2',
    'edc_t',
    'elastic1',
    'elastic2',
    'elasticband',
    'fossilfuel',
    'fossum',
    'frogs',
    'frostedflakes',
    'fruitohms',
    'gaba',
    'geophones',
    'grog',
    'head_injury',
    'hills',
    'hills2000',
    'hotspots',
    'hotspots2006',
    'houseprices',
    'humanpower1',
    'humanpower2',
    'hurric_named',
    'intersalt',
    'ironslag',
    'jobs',
    'kiwishade',
    'leafshape',
    'leafshape17',
    'leaftemp',
    'leaftemp_all',
    'litters',
    'lung',
    'measles',
    'med_expenses',
    'mifem',
    'mignonette',
    'milk',
    'modelcars',
    'monica',
    'moths',
    'nass_cds',
    'nasshead',
    'nihills',
    'nsw74demo',
    'nsw74psid1',
    'nsw74psid3',
    'nsw74psid_a',
    'nswdemo',
    'nswpsid1',
    'oddbooks',
    'orings',
    'pair65',
    'possum',
    'possumsites',
    'primates',
    'progression',
    'psid1',
    'psid2',
    'psid3',
    'races2000',
    'rainforest',
    'rareplants',
    'rice',
    'rock_art',
    'roller',
    'science',
    'seedrates',
    'socsupport',
    'softbacks',
    'sorption',
    'spam7',
    'st_vincent',
    'sugar',
    'tinting',
    'tomato',
    'toycars',
    'vince111b',
    'vlt',
    'wages1833',
    'world_records',
    'fars',
    'air_accs',
    'cvalues',
    'fars2007',
    'fars2008',
    'german',
    'loti',
    'alloauto',
    'allograft',
    'azt',
    'baboon',
    'bcdeter',
    'bfeed',
    'bmt',
    'bnct',
    'btrial',
    'burn',
    'drug6mp',
    'drughiv',
    'hodg',
    'kidrecurr',
    'kidtran',
    'larynx',
    'pneumon',
    'psych',
    'std',
    'stddiag',
    'tongue',
    'twins',
    'animals2',
    'crohn_d',
    'n_ox_emissions',
    'siegels_ex',
    'aircraft',
    'airmay',
    'alcohol',
    'ambient_noxch',
    'biomass_till',
    'bushfire',
    'carrots',
    'cloud',
    'coleman',
    'condroz',
    'cushny',
    'delivery',
    'education',
    'epilepsy',
    'ex_am',
    'foodstamp',
    'hbk',
    'heart',
    'kootenay',
    'lactic',
    'pension',
    'phosphor',
    'pilot',
    'possum_div',
    'pulpfiber',
    'radar_image',
    'stars_cyg',
    'telef',
    'toxicity',
    'vaso',
    'wagner_growth',
    'wood',
    'ams_survey',
    'adler',
    'angell',
    'us_public_school',
    'baumann',
    'bfox',
    'blackmore',
    'burt',
    'can_pop',
    'chile',
    'chirot',
    'cowles',
    'davis',
    'davis_thin',
    'depredations',
    'duncan',
    'ericksen',
    'florida',
    'freedman',
    'friendly',
    'ginzberg',
    'greene',
    'guyer',
    'hartnagel',
    'highway1',
    'kostecki_dillon',
    'leinhardt',
    'lo_bd',
    'mandel',
    'migration',
    'moore',
    'mroz',
    'o_brien_kaiser',
    'ornstein',
    'pottery',
    'prestige',
    'quartet',
    'robey',
    'slid',
    'sahlins',
    'salaries',
    'soils',
    'states',
    'transact',
    'un_gdp_infant_mortality',
    'us_pop',
    'vocab',
    'weight_loss',
    'womenlf',
    'wong',
    'wool1',
    'agriculture',
    'animals',
    'chor_sub',
    'flower',
    'plant_traits',
    'pluton',
    'ruspini',
    'votes_repub',
    'xclara',
    'affairs',
    'azcabgptca',
    'azdrg112',
    'azpro',
    'azprocedure',
    'badhealth',
    'fasttrakg',
    'fishing',
    'lbw',
    'lbwgrp',
    'loomis',
    'mdvis',
    'medpar',
    'nuts',
    'rwm',
    'rwm1984',
    'rwm5yr',
    'smoking',
    'titanicgrp',
    'accident',
    'airline',
    'airq',
    'benefits',
    'bids',
    'budget_food',
    'budget_italy',
    'budget_uk',
    'bwages',
    'cp_sch3',
    'cran_packages',
    'capm',
    'car',
    'caschool',
    'catsup',
    'cigar',
    'cigarette',
    'clothing',
    'computers',
    'cracker',
    'crime',
    'dm',
    'diamond',
    'doctor',
    'doctor_aus',
    'doctor_contacts',
    'earnings',
    'electricity',
    'fair',
    'fatality',
    'fishing1',
    'forward',
    'friend_foe',
    'garch',
    'gasoline',
    'griliches',
    'grunfeld',
    'hc_choice_california',
    'hhs_cyber_security_breaches',
    'hi_hours_worked',
    'hdma',
    'heating',
    'hedonic',
    'hmda',
    'housing',
    'icecream',
    'journals',
    'kakadu',
    'ketchup',
    'klein',
    'labor_supply',
    'labour',
    'mcas',
    'males',
    'mathlevel',
    'med_exp',
    'metal',
    'mode',
    'mode_choice',
    'mofa',
    'mroz1',
    'mun_exp',
    'natural_park',
    'nerlove',
    'ofp',
    'oil',
    'psid',
    'participation',
    'patents_hgh',
    'patents_rd',
    'pound',
    'produc',
    'ret_school',
    'sp500',
    'schooling',
    'somerville',
    'star',
    'strike',
    'strike_dur',
    'strike_nb',
    'tobacco',
    'train',
    'transp_eq',
    'treatment',
    'tuna1',
    'us_finance_industry',
    'us_gdp_presidents',
    'us_classified_documents',
    'us_state_abbreviations',
    'us_tax_words',
    'unemp_dur',
    'unemployment',
    'university',
    'vietnam_h',
    'vietnam_i',
    'wages',
    'wages1',
    'workinghours',
    'yen',
    'yogurt',
    'banking_crises',
    'breaches',
    'incidents_by_country_yr',
    'income_inequality',
    'nkill_by_country_yr',
    'non_english_names',
    'political_knowledge',
    'terrorism',
    'parkinsons',
    'aldh2',
    'apoeapoc',
    'cf',
    'crohn',
    'fa',
    'fsnps',
    'hla',
    'hr1420',
    'l51',
    'lukas',
    'mao',
    'meyer',
    'mfblong',
    'mhtdata',
    'nep499',
    'luv_colours',
    'arbuthnot',
    'armada',
    'bowley',
    'cavendish',
    'chest_sizes',
    'cholera',
    'cushny_peebles',
    'cushny_peebles_n',
    'dactyl',
    'drinks_wages',
    'fingerprints',
    'galton',
    'galton_families',
    'guerry',
    'halley_life_table',
    'jevons',
    'langren_all',
    'langren1644',
    'macdonell',
    'macdonell_df',
    'michelson',
    'michelson_sets',
    'minard_cities',
    'minard_temp',
    'minard_troops',
    'nightingale',
    'old_maps',
    'pearson_lee',
    'polio_trials',
    'prostitutes',
    'pyx',
    'quarrels',
    'snow_dates',
    'snow_deaths',
    'snow_deaths2',
    'snow_pumps',
    'snow_streets',
    'wheat',
    'wheat_monarchs',
    'yeast',
    'yeast_d_mat',
    'zea_mays',
    'barley',
    'environmental',
    'ethanol',
    'melanoma',
    'singer',
    'aids2',
    'animals1',
    'boston',
    'cars93',
    'cushings',
    'ddt_kale',
    'gag_urine',
    'insurance',
    'melanoma1',
    'ome_children',
    'pima_te',
    'pima_tr',
    'pima_tr2',
    'rabbit',
    'rubber',
    'sitka',
    'sitka89',
    'skye',
    'traffic',
    'us_cereal',
    'us_crime',
    'va_lung_cancer',
    'abbey',
    'accdeaths',
    'anorexia',
    'bacteria',
    'beav1',
    'beav2',
    'biopsy',
    'birthwt',
    'cabbages',
    'caith',
    'cats',
    'cement',
    'chem',
    'coop',
    'cpus',
    'crabs',
    'deaths',
    'drivers',
    'eagles',
    'epil',
    'farms',
    'fgl',
    'forbes',
    'galaxies',
    'gehan',
    'genotype',
    'geyser',
    'gilgais',
    'housing1',
    'immer',
    'leuk',
    'mammals',
    'mcycle',
    'menarche',
    'michelson1',
    'minn38',
    'motors',
    'muscle',
    'newcomb',
    'nlschools',
    'npr1',
    'oats',
    'painters',
    'petrol',
    'quine',
    'road',
    'rotifer',
    'ships',
    'shrimp',
    'shuttle',
    'snails',
    'steam',
    'stormer',
    'survey',
    'synth_te',
    'synth_tr',
    'topo',
    'waders',
    'whiteside',
    'wtloss',
    'empl_uk',
    'grunfeld1',
    'males1',
    'parity',
    'rice_farms',
    'snmesp',
    'sum_hes',
    'baseball',
    'australian_election_polling',
    'australian_elections',
    'efron_morris',
    'rock_the_vote',
    'uk_house_of_commons',
    'absentee',
    'admit',
    'bio_chemists',
    'ca2006',
    'iraq_vote',
    'political_information',
    'presidential_elections',
    'prussian',
    'union_density',
    'vote92',
    'french_fries',
    'tips',
    'car_test_frame',
    'car90',
    'cu_summary',
    'kyphosis',
    'solder',
    'stagec',
    'public_schools',
    'bollen',
    'cnes',
    'klein1',
    'mental_tests',
    'bladder',
    'cancer',
    'cgd',
    'colon',
    'flchain',
    'genfan',
    'kidney',
    'leukemia',
    'logan',
    'lung',
    'mgus',
    'mgus2',
    'myeloid',
    'nwtco',
    'ovarian',
    'pbc',
    'rats',
    'retinopathy',
    'rh_dnase',
    'stanford2',
    'tobin',
    'transplant',
    'veteran',
    'arthritis',
    'baseball1',
    'broken_marriage',
    'bundesliga',
    'bundestag2005',
    'butterfly',
    'coal_miners',
    'danish_welfare',
    'employment',
    'federalist',
    'hitters',
    'horse_kicks',
    'hospital',
    'job_satisfaction',
    'joint_sports',
    'lifeboats',
    'non_response',
    'ovary_cancer',
    'pre_sex',
    'punishment',
    'rep_vict',
    'saxony',
    'sexual_fun',
    'space_shuttle',
    'suicide',
    'trucks',
    'uk_soccer',
    'visual_acuity',
    'von_bort',
    'weldon_dice',
    'women_queue',
    'p_erisk',
    'supreme_court',
    'weimar',
    'approval',
    'bivariate',
    'coalition',
    'coalition2',
    'eidat',
    'free1',
    'free2',
    'friendship',
    'grunfeld2',
    'hoff',
    'homerun',
    'immi1',
    'immi2',
    'immi3',
    'immi4',
    'immi5',
    'immigration',
    'klein2',
    'kmenta2',
    'macro',
    'mexico',
    'mid',
    'newpainters',
    'sanction',
    'seatshare',
    'sna_ex',
    'turnout',
    'voteincome',
    'bcg_vaccine',
    'bthe_b',
    'cygob1',
    'forbes2000',
    'ghq',
    'lanza',
    'agefat',
    'aspirin',
    'birthdeathrates',
    'bladdercancer',
    'clouds',
    'foster',
    'heptathlon',
    'mastectomy',
    'meteo',
    'orallesions',
    'phosphate',
    'pistonrings',
    'planets',
    'plasma',
    'polyps',
    'polyps3',
    'pottery1',
    'rearrests',
    'respiratory',
    'roomwidth',
    'schizophrenia',
    'schizophrenia2',
    'schooldays',
    'skulls',
    'students',
    'suicides',
    'toothpaste',
    'voting',
    'water',
    'watervoles',
    'waves',
    'weightgain',
    'womensrole',
    'bechtoldt',
    'bechtoldt_1',
    'bechtoldt_2',
    'dwyer',
    'gleser',
    'gorsuch',
    'harman_5',
    'harman_8',
    'harman_political',
    'holzinger',
    'holzinger_9',
    'reise',
    'schmid',
    'schutz',
    'thurstone',
    'thurstone_33',
    'tucker',
    'ability',
    'affect',
    'bfi',
    'bfi_dictionary',
    'blot',
    'burt1',
    'cattell',
    'cities1',
    'cubits',
    'epi',
    'epi_bfi',
    'epi_dictionary',
    'galton1',
    'heights',
    'income',
    'iqitems',
    'msq',
    'neo',
    'peas',
    'sat_act',
    'within_between',
    'bosco',
    'cobar_ore',
    'mammals1',
    'barro',
    'engel',
    'gasprice',
    'uis',
    'dietox',
    'koch',
    'ohio',
    'respdis',
    'seizure',
    'spruce',
    'liver',
    'nidd',
    'portpirie',
    'rain',
    'summer',
    'wavesurge',
    'winter',
    'arthritis1',
    'bmw',
    'danish',
    'nidd_annual',
    'nidd_thresh',
    'siemens',
    'sp_raw',
    'spto87',
    'arabidopsis',
    'dyestuff',
    'dyestuff2',
    'pastes',
    'penicillin',
    'verb_agg',
    'cake',
    'cbpp',
    'grouseticks',
    'sleepstudy',
    'alcohol1',
    'birthdays',
    'births',
    'births78',
    'cps_85',
    'cooling_water',
    'countries',
    'dimes',
    'galton2',
    'gestation',
    'goose_permits',
    'help_full',
    'help_miss',
    'help_rct',
    'heat_x',
    'kids_feet',
    'marriage',
    'mites',
    'rail_trail',
    'riders',
    'sat_state',
    'saratoga_houses',
    'snow_gr',
    'swim_records',
    'ten_mile_race',
    'utilities',
    'utilities2',
    'whickham',
    'auto',
    'caravan',
    'carseats',
    'college',
    'default',
    'oj',
    'portfolio',
    'smarket',
    'wage',
    'weekly',
    'alfalfa',
    'archery_data',
    'auto_pollution',
    'backpack',
    'baseball_times',
    'bee_stings',
    'bird_nest',
    'blood1',
    'blue_jays',
    'british_unions',
    'cafe',
    'calcium_bp',
    'cancer_survival',
    'caterpillars',
    'cereal',
    'chemo_thc',
    'child_speaks',
    'cloud_seeding',
    'cloud_seeding2',
    'cracker_fiber',
    'cuckoo',
    'day1_survey',
    'diamonds',
    'diamonds2',
    'election08',
    'ethanol1',
    'fgb_y_distance',
    'fantasy_baseball',
    'fertility',
    'film',
    'final_four_izzo',
    'final_four_long',
    'final_four_short',
    'fingers',
    'first_year_gpa',
    'fish_eggs',
    'flight_response',
    'fluorescence',
    'fruit_flies',
    'goldenrod',
    'grocery',
    'gunnels',
    'hawk_tail',
    'hawk_tail2',
    'hawks',
    'hearing_test',
    'high_peaks',
    'hoops',
    'horse_prices',
    'houses',
    'icu',
    'infant_mortality',
    'insurance_vote',
    'jurors',
    'kids198',
    'leaf_hoppers',
    'leukemia1',
    'long_jump_olympics',
    'lost_letter',
    'mlb_2007_standings',
    'marathon',
    'markets',
    'math_enrollment',
    'math_placement',
    'med_gpa',
    'mental_health',
    'metabolic_rate',
    'metro_health83',
    'milgram',
    'moth_eggs',
    'n_cbirths',
    'n_f_l2007_standings',
    'nursing',
    'olives',
    'orings1',
    'overdrawn',
    'palm_beach',
    'pedometer',
    'perch',
    'pig_feed',
    'pines',
    'political',
    'pollster08',
    'popcorn',
    'porsche_jaguar',
    'porsche_price',
    'pulse',
    'putts1',
    'putts2',
    'religion_gdp',
    'retirement',
    'river_elements',
    'river_iron',
    'sat_gpa',
    'sample_fg',
    'sandwich_ants',
    'sea_slugs',
    'sparrows',
    'species_area',
    'speed',
    'swahili',
    'tms',
    'text_prices',
    'three_cars',
    'tip_joke',
    'tomlinson_rush',
    'twins_lungs',
    'us_stamps',
    'volts',
    'walking_babies',
    'weight_loss_incentive',
    'weight_loss_incentive4',
    'weight_loss_incentive7',
    'word_memory',
    'youth_risk2007',
    'youth_risk2009',
    'indian_irish',
    'mendel_abc',
    'chain',
    'nlsy_v',
    'ced_data',
    'boundsdata',
    'framing',
    'school',
    'student',
    'admnrev',
    'airfare',
    'apple',
    'athlet1',
    'athlet2',
    'attend',
    'audit',
    'barium',
    'beauty',
    'benefits1',
    'beveridge',
    'big9salary',
    'bwght',
    'bwght2',
    'campus',
    'card',
    'ceosal1',
    'ceosal2',
    'charity',
    'consump',
    'corn',
    'cps78_85',
    'cps91',
    'crime1',
    'crime2',
    'crime3',
    'crime4',
    'discrim',
    'driving',
    'earns',
    'elem94_95',
    'engin',
    'expendshares',
    'ezanders',
    'ezunem',
    'fair1',
    'fertil1',
    'fertil2',
    'fertil3',
    'fish',
    'fringe',
    'gpa1',
    'gpa2',
    'gpa3',
    'happiness',
    'hprice1',
    'hprice2',
    'hprice3',
    'hseinv',
    'htv',
    'infmrt',
    'injury',
    'intdef',
    'intqrt',
    'inven',
    'jtrain',
    'jtrain2',
    'jtrain3',
    'kielmc',
    'lawsch85',
    'loanapp',
    'lowbrth',
    'mathpnl',
    'meap00_01',
    'meap01',
    'meap93',
    'minwage',
    'mlb1',
    'mroz2',
    'murder',
    'nbasal',
    'nyse',
    'okun',
    'openness',
    'phillips',
    'pntsprd',
    'prison',
    'prminwge',
    'rdchem',
    'rdtelec',
    'recid',
    'rental',
    'company_return',
    'saving',
    'sleep75',
    'slp75_81',
    'smoke',
    'traffic1',
    'traffic2',
    'twoyear',
    'volat',
    'vote1',
    'vote2',
    'voucher',
    'wage1',
    'wage2',
    'wagepan',
    'wageprc',
    'wine'

]

# Remove all extra symbols that don't have a docstring or are not explicitly
# referenced in the whitelist.
remove_undocumented(__name__, _allowed_symbols)