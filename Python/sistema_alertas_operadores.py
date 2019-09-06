import pandas as pd
import numpy as np
from datetime import date, timedelta
import os


class Operaciones:
    def __init__(
        self,
        file_status_x_dia_an,                                                   # Nombre del archivo que contiene la data de AN x dia
        file_status_x_dia_dv360,                                                # Nombre del archivo que contiene la data de DV360 x dia
        file_status_x_dia_gral,                                                 # Nombre del archivo que va a contener toda la data x dia
        file_status_an,                                                         # Nombre del archivo que contiene la data de AN por linea
        file_status_dv360,                                                      # Nombre del archivo que contiene la data de DV360 por linea
        file_status_gral,                                                       # Nombre del archivo que va a contener toda la data
        hf_line_id,                                                             # Header Final
        hf_adv,                                                                 # Header Final
        hf_campaign,                                                            # Header Final
        hf_dsp,                                                                 # Header Final
        hf_agencia,                                                             # Header Final
        hf_profit,                                                              # Header Final
        hf_pacing_teorico,                                                      # Header Final
        hf_pacing,                                                              # Header Final
        hf_last_day_vs_budget,                                                  # Header Final
        hf_kpi_total_pacing,                                                    # Header Final
        hf_kpi_last_day_vs_kpi_obj,                                             # Header Final
        hf_revenue,                                                             # Header Final
        hf_costo,                                                               # Header Final
        hf_profit_porcentaje,                                                   # Header Final
        hf_sm,                                                                  # Header Final
        hf_metrica_a_entregar,                                                  # Header Final
        hf_contratado_total_a_entregar,                                         # Header Final
        hf_entregado_hasta_ayer,                                                # Header Final
        hf_contratado_por_dia,                                                  # Header Final
        hf_entregado_ayer_value,                                                # Header Final
        hf_entrega,                                                             # Header Final
        hf_entrega_diaria,                                                      # Header Final
        hf_kpi,                                                                 # Header Final
        hf_kpi_dia_anterior,                                                    # Header Final
        hf_kpi_total_vs_kpi_obj,                                                # Header Final
        hf_dias_end,                                                            # Header Final
        hf_trader,                                                              # Header Final
        hf_revisada,                                                            # Header Final
        hf_comentarios,                                                         # Header Final
        hf_control,                                                             # Proporciona la informacion para saber como evaluar el KPI en relación a las alertas
        hf_revenue_lastday,                                                     # Header Final
        hf_sm_Value,                                                            # Header Final
        hf_Start_date,                                                          # Header Final
        hf_End_date,                                                            # Header Final
        hf_KPI,                                                                 # Header Final
        hf_KPI_Objetivo,                                                        # Header Final
        hn_date,                                                                # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_imps,                                                                # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_clicks,                                                              # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_ctr,                                                                 # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_conversions,                                                         # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_cost,                                                                # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_imps_viewed,                                                         # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_view_rate,                                                           # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_conv_rate,                                                           # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_completion_rate,                                                     # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_completions,                                                         # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_tview_rate,                                                          # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_tview_views,                                                         # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_duracion_dias,                                                       # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_date_last_day,                                                       # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_imps_last_day,                                                       # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_clicks_last_day,                                                     # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_ctr_last_day,                                                        # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_conversions_last_day,                                                # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_cost_last_day,                                                       # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_imps_viewed_last_day,                                                # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_view_rate_last_day,                                                  # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_conv_rate_last_day,                                                  # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_completion_rate_last_day,                                            # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_completions_last_day,                                                # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_tview_rate_last_day,                                                 # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
        hn_tview_views_last_day,                                                # Header de "file_status_gral" o "file_status_x_dia_gral" para realizar calculos
    ):
        self.file_status_x_dia_an = file_status_x_dia_an
        self.file_status_x_dia_dv360 = file_status_x_dia_dv360
        self.file_status_x_dia_gral = file_status_x_dia_gral
        self.file_status_an = file_status_an
        self.file_status_dv360 = file_status_dv360
        self.file_status_gral = file_status_gral
        self.hf_line_id = hf_line_id
        self.hf_adv = hf_adv
        self.hf_campaign = hf_campaign
        self.hf_dsp = hf_dsp
        self.hf_agencia = hf_agencia
        self.hf_profit = hf_profit
        self.hf_pacing_teorico = hf_pacing_teorico
        self.hf_pacing = hf_pacing
        self.hf_last_day_vs_budget = hf_last_day_vs_budget
        self.hf_kpi_total_pacing = hf_kpi_total_pacing
        self.hf_kpi_last_day_vs_kpi_obj = hf_kpi_last_day_vs_kpi_obj
        self.hf_revenue = hf_revenue
        self.hf_costo = hf_costo
        self.hf_profit_porcentaje = hf_profit_porcentaje
        self.hf_sm = hf_sm
        self.hf_metrica_a_entregar = hf_metrica_a_entregar
        self.hf_contratado_total_a_entregar = hf_contratado_total_a_entregar
        self.hf_entregado_hasta_ayer = hf_entregado_hasta_ayer
        self.hf_contratado_por_dia = hf_contratado_por_dia
        self.hf_entregado_ayer_value = hf_entregado_ayer_value
        self.hf_entrega = hf_entrega
        self.hf_entrega_diaria = hf_entrega_diaria
        self.hf_kpi = hf_kpi
        self.hf_kpi_dia_anterior = hf_kpi_dia_anterior
        self.hf_kpi_total_vs_kpi_obj = hf_kpi_total_vs_kpi_obj
        self.hf_dias_end = hf_dias_end
        self.hf_trader = hf_trader
        self.hf_revisada = hf_revisada
        self.hf_comentarios = hf_comentarios
        self.hf_control = hf_control
        self.hf_revenue_lastday = hf_revenue_lastday
        self.hf_sm_Value = hf_sm_Value
        self.hf_Start_date = hf_Start_date
        self.hf_End_date = hf_End_date
        self.hf_KPI = hf_KPI
        self.hf_KPI_Objetivo = hf_KPI_Objetivo
        self.hn_date = hn_date
        self.hn_imps = hn_imps
        self.hn_clicks = hn_clicks
        self.hn_ctr = hn_ctr
        self.hn_conversions = hn_conversions
        self.hn_cost = hn_cost
        self.hn_imps_viewed = hn_imps_viewed
        self.hn_view_rate = hn_view_rate
        self.hn_conv_rate = hn_conv_rate
        self.hn_completion_rate = hn_completion_rate
        self.hn_completions = hn_completions
        self.hn_tview_rate = hn_tview_rate
        self.hn_tview_views = hn_tview_views
        self.hn_duracion_dias = hn_duracion_dias
        self.hn_date_last_day = hn_date_last_day
        self.hn_imps_last_day = hn_imps_last_day
        self.hn_clicks_last_day = hn_clicks_last_day
        self.hn_ctr_last_day = hn_ctr_last_day
        self.hn_conversions_last_day = hn_conversions_last_day
        self.hn_cost_last_day = hn_cost_last_day
        self.hn_imps_viewed_last_day = hn_imps_viewed_last_day
        self.hn_view_rate_last_day = hn_view_rate_last_day
        self.hn_conv_rate_last_day = hn_conv_rate_last_day
        self.hn_completion_rate_last_day = hn_completion_rate_last_day
        self.hn_completions_last_day = hn_completions_last_day
        self.hn_tview_rate_last_day = hn_tview_rate_last_day
        self.hn_tview_views_last_day = hn_tview_views_last_day

    def yesterday_date(self):
        """
        Esta funcion se encarga de generar la fecha del dia anterior.
        """
        global yesterday
        yesterday = date.today() - timedelta(days=1)                            # Fecha ayer

    def errores_files(
        self,
        error_file_csv_an,                                                      # Nombre del archivo que contiene las lineas con errores de AN que no son tenidas en cuenta
        error_file_csv_dv360,                                                   # Nombre del archivo que contiene las lineas con errores de DV360 que no son tenidas en cuenta
        error_file_csv_tracker,                                                 # Nombre del archivo que contiene las lineas con errores del tracker
        errores_file_gral                                                       # Nombre del archivo donde se van a almacenar todas las lineas con errores
    ):
        """
        Esta funcion se encarga de agrupar los tres CSVs con errores (an, dv360 y tracker) para agruparlos en uno
        solo y de esta forma generar un único archivo que contenga todas las lineas con errores.
        Una vez generado el archivo general se eliminan los CSVs de materia prima.
        """
        try:
            errores_an = pd.read_csv(error_file_csv_an)                             # Abrimos el archivo error_file_csv_an
            errores_dv360 = pd.read_csv(error_file_csv_dv360)                       # Abrimos el archivo error_file_csv_dv360
            errores_tracker = pd.read_csv(error_file_csv_tracker)                   # Abrimos el archivo error_file_csv_tracker
            errores_all = pd.concat(                                                # Agrupamos los tres DataFrames en uno general
                [
                    errores_an,
                    errores_dv360,
                    errores_tracker
                ]
            )
            errores_all.to_csv(errores_file_gral, index=False)                      # Guardamos el DataFrame agrupado
            for file in [                                                           # removemos los 3 archivos anteriores
                error_file_csv_an,
                error_file_csv_dv360,
                error_file_csv_tracker
            ]:
                os.remove(file)                                                     # Remueve el archivo
        except Exception as e:
            print(e)

    def concat_dsps_files(self):
        """
        Esta funcion se encarga de unificar los CSV x días de las dos plataformas en un DataFrame General
        """
        global st_dias
        status_an_dias = pd.read_csv(self.file_status_x_dia_an)                 # Abrimos "file_status_x_dia_an"
        status_dv360_dias = pd.read_csv(self.file_status_x_dia_dv360)           # Abrimos "file_status_x_dia_dv360"
        st_dias = pd.concat([status_an_dias, status_dv360_dias])                # Unificamos los dos DataFrames en uno
        st_dias[self.hn_date] = pd.to_datetime(
            st_dias[self.hn_date],
            format="%Y/%m/%d"
        )
        st_dias = st_dias.sort_values(by=[self.hn_date])                        # Ordenamos por fecha ascendente, parte clave de la funcion ya que de esta forma obtendremos el ultimo día real en el que vimos impresiones
        st_dias.to_csv(self.file_status_x_dia_gral, index=False)                # Guardamos el DataFrame generado, y lo hacemos global para poder utilizarlo en otras funciones

    def last_day_lineas_file(
        self,
        last_day_x_linea
    ):
        dias = []                                                               # Lista donde vamos a almacenar los ultimos dias con impresiones del dataframe
        headers = [
            self.hf_line_id,
            self.hn_date_last_day,
            self.hn_imps_last_day,
            self.hn_clicks_last_day,
            self.hn_ctr_last_day,
            self.hn_conversions_last_day,
            self.hn_cost_last_day,
            self.hn_imps_viewed_last_day,
            self.hn_view_rate_last_day,
            self.hn_conv_rate_last_day,
            self.hn_completion_rate_last_day,
            self.hn_completions_last_day,
            self.hn_tview_rate_last_day,
            self.hn_tview_views_last_day
        ]
        df = [                                                                  # Agrupamos por "hf_line_id" para poder recolectar el ultimo dia por linea
            x for _,
            x in st_dias.groupby(self.hf_line_id)
        ]
        for linea in df:                                                         # Por cada linea realizamos las siguientes operaciones
            linea[self.hn_date] = pd.to_datetime(linea[self.hn_date])
            linea = linea.sort_values(by=self.hn_date, ascending=True)
            linea = linea.tail(1)
            linea = linea[[
                self.hf_line_id,
                self.hn_date,
                self.hn_imps,
                self.hn_clicks,
                self.hn_ctr,
                self.hn_conversions,
                self.hn_cost,
                self.hn_imps_viewed,
                self.hn_view_rate,
                self.hn_conv_rate,
                self.hn_completion_rate,
                self.hn_completions,
                self.hn_tview_rate,
                self.hn_tview_views
            ]]
            lista = linea.values
            for item2 in lista:
                dias.append(item2)
        df = pd.DataFrame(dias, columns=headers)
        df.to_csv(last_day_x_linea, index=False)

        status_an = pd.read_csv(self.file_status_an)
        status_dv360 = pd.read_csv(self.file_status_dv360)
        st = [status_an, status_dv360]
        st = pd.concat(st)
        st = st.merge(df, how='left')
        st.to_csv(self.file_status_gral, index=False)

    def calculos(
        self,
        valor_dolar,
        valor_dolar_carrefour,
        cero_dias,
        sm_type_CPCV,
        sm_type_CPCV100,
        sm_type_TV,
        sm_type_CPE,
        sm_type_CPM,
        sm_type_CPC,
        sm_type_vCPM,
        fin_ok_entrega,
        fin_insf_entrega,
        fin_notyet_entrega,
        hf_estado,
        kpi_type_Viewability,
        kpi_type_CTR,
        kpi_type_CompletionRate,
        kpi_type_TrueViewRate,
        kpi_type_Clicks,
        kpi_type_Impressions,
        kpi_type_Alcance,
        kpi_type_Reach,
        kpi_type_Conversions,
        kpi_type_CompleteViews,
        kpi_type_CPC,
        control_alerta,
        control_ok,
        control_exceso,
        control_normal,
        control_inverso,
        pacing_alerta_value,
        pacing_exceso_value,
        profit_alerta,
    ):
        st = pd.read_csv(self.file_status_gral)
        # Astypes - START ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        for col in [
            self.hf_contratado_total_a_entregar,
            self.hn_imps,
            self.hn_clicks,
            self.hn_conversions,
            self.hn_imps_viewed,
            self.hn_completions,
            self.hn_tview_views
        ]:
            st[col] = st[col].astype(int)                                               # Columnas a Int

        for col in [
            self.hf_sm_Value,
            self.hn_cost,
            self.hn_view_rate,
            self.hn_ctr,
            self.hn_conv_rate,
            self.hn_completion_rate,
            self.hn_tview_rate
        ]:
            st[col] = st[col].astype(float)                                             # Columnas a Float

        for col in [
            self.hf_Start_date,
            self.hf_End_date
        ]:
            st[col] = pd.to_datetime(
                st[col]
            ).dt.date                                                                   # Columnas a Datetime
        # Astypes - END ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Conversion de pesos a dolares - START ----------------------------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_dsp] == 'DBM', self.hn_cost
        ] = st[self.hn_cost] / valor_dolar                                                   # Si el DSP es DBM, como esta en pesos argentinos el costo debemos pasarlo a dolares

        # Conversion de pesos a dolares - END ------------------------------------------------------------------------------------------------------------------------------------------------------

        # Calculos sobre duración de la campaña - START --------------------------------------------------------------------------------------------------------------------------------------------
        st[self.hn_duracion_dias] = \
            st[self.hf_End_date] - st[self.hf_Start_date]                                         # Cantidad de dias que dura la campaña

        st_dias_transcurridos = \
            yesterday - st[self.hf_Start_date]                                               # Cantidad de dias transcurridos

        st[self.hf_dias_end] = \
            st[self.hf_End_date] - yesterday                                                 # Cantidad de dias restantes
        st[self.hf_dias_end] = st[self.hf_dias_end].dt.days

        st.loc[
            st[self.hf_dias_end] <= cero_dias,
            self.hf_dias_end
        ] = cero_dias                                                                           # Modifica la columna de dias restantes, si la campaña ya termino en vez de darnos un valor negativo nos da 0 en dias restantes

        st[self.hf_pacing_teorico] = st_dias_transcurridos / (
            st[self.hf_End_date] - st[self.hf_Start_date]
        )                                                                               # Pacing en dias teorico
        # Calculos sobre duración de la campaña - END ----------------------------------------------------------------------------------------------------------------------------------------------

        # Calculos dependiendo del Cell Metric - START ---------------------------------------------------------------------------------------------------------------------------------------------
        # CPCV-----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_sm] == sm_type_CPCV, self.hf_metrica_a_entregar
        ] = self.hn_completions                                                              # Metrica a entregar (ej: Impressions)
        st.loc[
            st[self.hf_sm] == sm_type_CPCV, self.hf_entregado_hasta_ayer
        ] = st[self.hn_completions]                                                          # Entrega Total Realizada
        st.loc[
            st[self.hf_sm] == sm_type_CPCV, self.hf_entregado_ayer_value
        ] = st['{} LastDay'.format(self.hn_completions)]                                     # Entrega Ayer
        st.loc[
            st[self.hf_sm] == sm_type_CPCV, self.hf_revenue
        ] = st[self.hf_entregado_hasta_ayer] * st[self.hf_sm_Value]                               # Revenue Total

        # CPCV100-----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_sm] == sm_type_CPCV100, self.hf_metrica_a_entregar
        ] = self.hn_completions                                                              # Metrica a entregar (ej: Impressions)
        st.loc[
            st[self.hf_sm] == sm_type_CPCV100, self.hf_entregado_hasta_ayer
        ] = st[self.hn_completions]                                                          # Entrega Total Realizada
        st.loc[
            st[self.hf_sm] == sm_type_CPCV100, self.hf_entregado_ayer_value
        ] = st['{} LastDay'.format(self.hn_completions)]                                     # Entrega Ayer
        st.loc[
            st[self.hf_sm] == sm_type_CPCV100, self.hf_revenue
        ] = st[self.hf_entregado_hasta_ayer] * st[self.hf_sm_Value]                               # Revenue Total

        # CPE-----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_sm] == sm_type_CPE, self.hf_metrica_a_entregar
        ] = self.hn_completions                                                              # Metrica a entregar (ej: Impressions)
        st.loc[
            st[self.hf_sm] == sm_type_CPE, self.hf_entregado_hasta_ayer
        ] = st[self.hn_completions]                                                          # Entrega Total Realizada
        st.loc[
            st[self.hf_sm] == sm_type_CPE, self.hf_entregado_ayer_value
        ] = st['{} LastDay'.format(self.hn_completions)]                                     # Entrega Ayer
        st.loc[
            st[self.hf_sm] == sm_type_CPE, self.hf_revenue
        ] = st[self.hf_entregado_hasta_ayer] * st[self.hf_sm_Value]                               # Revenue Total

        # TV-----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_sm] == sm_type_TV, self.hf_metrica_a_entregar
        ] = self.hn_tview_views                                                              # Metrica a entregar (ej: Impressions)
        st.loc[
            st[self.hf_sm] == sm_type_TV, self.hf_entregado_hasta_ayer
        ] = st[self.hn_tview_views]                                                          # Entrega Total Realizada
        st.loc[
            st[self.hf_sm] == sm_type_TV, self.hf_entregado_ayer_value
        ] = st['{} LastDay'.format(self.hn_tview_views)]                                     # Entrega Ayer
        st.loc[
            st[self.hf_sm] == sm_type_TV, self.hf_revenue
        ] = st[self.hf_entregado_hasta_ayer] * st[self.hf_sm_Value]                               # Revenue Total

        # CPM-----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_sm] == sm_type_CPM, self.hf_metrica_a_entregar
        ] = self.hn_imps                                                                     # Metrica a entregar (ej: Impressions)
        st.loc[
            st[self.hf_sm] == sm_type_CPM, self.hf_entregado_hasta_ayer
        ] = st[self.hn_imps]                                                                 # Entrega Total Realizada
        st.loc[
            st[self.hf_sm] == sm_type_CPM, self.hf_entregado_ayer_value
        ] = st['{} LastDay'.format(self.hn_imps)]                                            # Entrega Ayer
        st.loc[
            st[self.hf_sm] == sm_type_CPM, self.hf_revenue
        ] = (
            st[self.hf_entregado_hasta_ayer] * st[self.hf_sm_Value]
        ) / 1000                                                                        # Revenue Total

        # vCPM-----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_sm] == sm_type_vCPM, self.hf_metrica_a_entregar
        ] = self.hn_imps_viewed                                                              # Metrica a entregar (ej: Impressions)
        st.loc[
            st[self.hf_sm] == sm_type_vCPM, self.hf_entregado_hasta_ayer
        ] = st[self.hn_imps_viewed]                                                          # Entrega Total Realizada
        st.loc[
            st[self.hf_sm] == sm_type_vCPM, self.hf_entregado_ayer_value
        ] = st['{} LastDay'.format(self.hn_imps_viewed)]                                     # Entrega Ayer
        st.loc[
            st[self.hf_sm] == sm_type_vCPM, self.hf_revenue
        ] = (
            st[self.hf_entregado_hasta_ayer] * st[self.hf_sm_Value]
        ) / 1000                                                                        # Revenue Total

        # CPC-----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_sm] == sm_type_CPC, self.hf_metrica_a_entregar
        ] = self.hn_clicks                                                                   # Metrica a entregar (ej: Impressions)
        st.loc[
            st[self.hf_sm] == sm_type_CPC, self.hf_entregado_hasta_ayer
        ] = st[self.hn_clicks]                                                               # Entrega Total Realizada
        st.loc[
            st[self.hf_sm] == sm_type_CPC, self.hf_entregado_ayer_value
        ] = st['{} LastDay'.format(self.hn_clicks)]                                          # Entrega Ayer
        st.loc[
            st[self.hf_sm] == sm_type_CPC, self.hf_revenue
        ] = st[self.hf_entregado_hasta_ayer] * st[self.hf_sm_Value]                               # Revenue Total
        st.loc[
            st[self.hf_sm] == sm_type_CPC, self.hf_revenue_lastday
        ] = st['{} LastDay'.format(self.hn_clicks)] * st[self.hf_sm_Value]                        # Revenue Last Day
        # Calculos dependiendo del Cell Metric - END -----------------------------------------------------------------------------------------------------------------------------------------------

        # Correccion Revenue para Carrefour - START ------------------------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            (
                st[self.hf_dsp].str.contains("DBM")
            ) & (
                st[self.hf_adv].str.contains("Carrefour")), self.hf_revenue
        ] = (
            valor_dolar_carrefour * st[self.hf_revenue]
        ) / valor_dolar

        st.loc[
            (
                st[self.hf_dsp].str.contains("DBM")
            ) & (
                st[self.hf_adv].str.contains("Carrefour")), self.hf_revenue_lastday
        ] = (
            valor_dolar_carrefour * st[self.hf_revenue_lastday]
        ) / valor_dolar
        # Correccion Revenue para Carrefour - END --------------------------------------------------------------------------------------------------------------------------------------------------

        # Calculos Generales - START ---------------------------------------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            (
                st[self.hf_dias_end] == cero_dias
            ) & (
                st[self.hf_entregado_hasta_ayer] >= (
                    st[self.hf_contratado_total_a_entregar]
                ) * 0.95
            ), hf_estado
        ] = fin_ok_entrega
        st.loc[
            (
                st[self.hf_dias_end] == cero_dias
            ) & (
                st[self.hf_entregado_hasta_ayer] < (
                    st[self.hf_contratado_total_a_entregar]
                ) * 0.95
            ), hf_estado
        ] = fin_insf_entrega
        st.loc[
            st[self.hf_dias_end] > cero_dias, hf_estado
        ] = fin_notyet_entrega

        st[self.hf_contratado_por_dia] = (
            st[self.hf_contratado_total_a_entregar] -
            st[self.hf_entregado_hasta_ayer]
        ) / st[self.hf_dias_end]                                                       # Contratado teorico por dia, es el valor de impresiones que se deberian entregar por dia teniendo en cuenta la cantidad entregada hasta el momento

        st.loc[
            (
                st[self.hf_contratado_por_dia] == np.inf
            ),
            self.hf_contratado_por_dia] = (
                st[self.hf_contratado_total_a_entregar] -
                st[self.hf_entregado_hasta_ayer]
        )                                                                                           # Si es Inf el valor que hay en el contratado teorico por dia, proviene de dividir el monto que nos quedo pendiente para entregar por 0.

        st.loc[
            st[self.hf_contratado_por_dia] < 0,
            self.hf_contratado_por_dia
        ] = 0                                                                                       # Si la campaña ya entrego todo lo que tenia como objetivo, en vez de aparecer un numero negativo a entregar por dia colocamos 0

        st.loc[
            (
                st[self.hf_dias_end] <= cero_dias
            ) & (
                st[self.hf_entregado_hasta_ayer] <
                st[self.hf_contratado_total_a_entregar]
            ),
            self.hf_entrega
        ] = np.nan                                                             # Si la campaña finalizo en dias pero nos quedamos cortos en la entrega, la columna del % Pacing la dejamos como nan

        st.loc[
            st[self.hf_dias_end] > cero_dias,
            self.hf_entrega
        ] = (
            st[self.hf_entregado_hasta_ayer] /
            st[self.hf_contratado_total_a_entregar]
        )                                                                      # Si la campaña no finalizo en dias el % Pacing se ejecuta y nos da la cuenta en % de lo entregado hasta ayer dividido el objetivo

        st.loc[
            st[self.hf_entrega] >= 1,
            self.hf_entrega
        ] = np.inf                                                              # asdasdasdasdasd
        st.loc[
            st[self.hf_entrega] < 1,
            self.hf_entrega
        ] = st[self.hf_entrega] - st[self.hf_pacing_teorico]
        st.loc[
            (
                1 <= st[self.hf_entrega]
            ) & (
                st[self.hf_entrega] < np.inf
            ),
            self.hf_entrega
        ] = 1 - st[self.hf_entrega]

        st[self.hf_entrega_diaria] = (
            st[self.hf_entregado_ayer_value] -
            st[self.hf_contratado_por_dia]
        ) / st[self.hf_contratado_por_dia]                                           # Pacing % Por dia

        st[self.hf_profit_porcentaje] = (
            1 - (
                st[self.hn_cost] / st[self.hf_revenue]
            )
        )                                                                       # Profit Total

        # Calculos Generales - END -----------------------------------------------------------------------------------------------------------------------------------------------------------------

        # KPIS
        # KPI - Viewability -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_Viewability, self.hf_kpi
        ] = st[self.hn_view_rate]                                                                # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_Viewability, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hf_kpi] -
            (
                st[self.hf_KPI_Objetivo]
            ) * 0.01
        )                                                                                   # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_Viewability, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_view_rate)]                                           # El valor del KPI entregado Last Day
        st.loc[st[self.hf_KPI] == kpi_type_Viewability, self.hf_control] = control_normal                                              # Control (es para saber como calcular el Alerta de KPI)

        # KPI - CTR -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_CTR, self.hf_kpi
        ] = st[self.hn_ctr]                                    # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_CTR, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hf_kpi] -
            (
                st[self.hf_KPI_Objetivo]
            ) * 0.01
        )                                                                                   # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_CTR, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_ctr)]                                                 # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_CTR, self.hf_control
        ] = control_normal                                                                  # Control (es para saber como calcular el Alerta de KPI)

        # KPI - Completion Rate (VTR) -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_CompletionRate, self.hf_kpi
        ] = st[self.hn_completion_rate]                                                          # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_CompletionRate, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hf_kpi] -
            (
                st[self.hf_KPI_Objetivo]
            ) * 0.01
        )                                                                                   # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_CompletionRate, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_completion_rate)]                                     # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_CompletionRate, self.hf_control
        ] = control_normal                                                                  # Control (es para saber como calcular el Alerta de KPI)

        # KPI - TruewViews Rate -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_TrueViewRate, self.hf_kpi
        ] = st[self.hn_tview_rate]                    # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_TrueViewRate, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hf_kpi] -
            (
                st[self.hf_KPI_Objetivo]
            ) * 0.01
        )                                                                                   # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_TrueViewRate, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_tview_rate)]                                          # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_TrueViewRate, self.hf_control
        ] = control_normal                                                                  # Control (es para saber como calcular el Alerta de KPI)

        # KPI - Clicks -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_Clicks, self.hf_kpi
        ] = st[self.hn_clicks]                                                                   # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_Clicks, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hn_clicks] /
            st[self.hf_KPI_Objetivo]
        ) - st[self.hf_pacing_teorico]                                                           # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_Clicks, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_clicks)]                                              # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_Clicks, self.hf_control
        ] = control_normal                                                                  # Control (es para saber como calcular el Alerta de KPI)

        # KPI - Impresiones -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_Impressions, self.hf_kpi
        ] = st[self.hn_imps]                                                                     # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_Impressions, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hn_imps] /
            st[self.hf_KPI_Objetivo]
        ) - st[self.hf_pacing_teorico]                                                           # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_Impressions, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_imps)]                                                # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_Impressions, self.hf_control
        ] = control_normal                                                                  # Control (es para saber como calcular el Alerta de KPI)

        # KPI - Alcance -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_Alcance, self.hf_kpi
        ] = st[self.hn_imps]                                                                     # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_Alcance, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hn_imps] /
            st[self.hf_KPI_Objetivo]
        ) - st[self.hf_pacing_teorico]                                                           # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_Alcance, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_imps)]                                                # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_Alcance, self.hf_control
        ] = control_normal                                                                  # Control (es para saber como calcular el Alerta de KPI)

        # KPI - Reach -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_Reach, self.hf_kpi
        ] = st[self.hn_imps]                                                                     # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_Reach, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hn_imps] /
            st[self.hf_KPI_Objetivo]
        ) - st[self.hf_pacing_teorico]                                                           # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_Reach, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_imps)]                                                # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_Reach, self.hf_control
        ] = control_normal                                                                  # Control (es para saber como calcular el Alerta de KPI)

        # KPI - Conversiones -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_Conversions, self.hf_kpi
        ] = st[self.hn_conversions]                                                              # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_Conversions, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hn_conversions] /
            st[self.hf_KPI_Objetivo]
        ) - st[self.hf_pacing_teorico]                                                           # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_Conversions, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_conversions)]                                         # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_Conversions, self.hf_control
        ] = control_normal                                                                  # Control (es para saber como calcular el Alerta de KPI)

        # KPI - Complete Views -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_CompleteViews, self.hf_kpi
        ] = st[self.hn_completions]                                                              # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_CompleteViews, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hn_completions] /
            st[self.hf_KPI_Objetivo]
        ) - st[self.hf_pacing_teorico]                                                           # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_CompleteViews, self.hf_kpi_dia_anterior
        ] = st['{} LastDay'.format(self.hn_completions)]                                     # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_CompleteViews, self.hf_control
        ] = control_normal                                            # Control (es para saber como calcular el Alerta de KPI)

        # KPI - CPC -----------------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_KPI] == kpi_type_CPC, self.hf_kpi
        ] = (
            st[self.hf_revenue] /
            st[self.hn_clicks]
        ) * valor_dolar                                                                                 # El valor del KPI a entregado Total (ej: 90.00%)
        st.loc[
            st[self.hf_KPI] == kpi_type_CPC, self.hf_kpi_total_vs_kpi_obj
        ] = (
            st[self.hf_kpi] -
            st[self.hf_KPI_Objetivo]
        )                                                # Comparacion de KPI total vs KPI Objetivo
        st.loc[
            st[self.hf_KPI] == kpi_type_CPC, self.hf_kpi_dia_anterior
        ] = (
            st[self.hf_revenue_lastday] /
            st['{} LastDay'.format(self.hn_completions)]
        ) * valor_dolar                  # El valor del KPI entregado Last Day
        st.loc[
            st[self.hf_KPI] == kpi_type_CPC, self.hf_control
        ] = control_inverso                                                     # Control (es para saber como calcular el Alerta de KPI)

        # ALERTAS
        # Alerta Profit START -------------------------------------------------------------------------------------------------------------------------
        st.loc[
            st[self.hf_profit_porcentaje] >= profit_alerta,
            self.hf_profit
        ] = control_ok                                                                                # Alerta Profit, si es mayor o igual al 70% esta OK
        st.loc[
            st[self.hf_profit_porcentaje] < profit_alerta,
            self.hf_profit
        ] = control_alerta                                                         # Alerta Profit, si es menor al 70% esta Alerta
        # Alerta Profit END ---------------------------------------------------------------------------------------------------------------------------

        # Alerta Pacing START -------------------------------------------------------------------------------------------------------------------------
        st.loc[
            (
                (
                    pacing_alerta_value <= st[self.hf_entrega]
                ) & (
                    st[self.hf_entrega] < pacing_exceso_value
                )
            ), self.hf_pacing
        ] = control_ok                                                                                # Alerta Pacing Total, si esta entre -5% y 20% esta ok
        st.loc[
            st[self.hf_entrega] >= pacing_exceso_value,
            self.hf_pacing
        ] = control_exceso                                                         # Alerta Pacing Total, si es mayor a 20% Exceso
        st.loc[
            st[self.hf_entrega] < pacing_alerta_value,
            self.hf_pacing
        ] = control_alerta                                                        # Alerta Pacing Total, si es menor al -5% Alerta
        # Alerta Pacing END ---------------------------------------------------------------------------------------------------------------------------

        # Alerta Pacing Last Day - START --------------------------------------------------------------------------------------------------------------
        st.loc[
            (
                (
                    pacing_alerta_value <= st[self.hf_entrega_diaria]
                ) & (
                    st[self.hf_entrega_diaria] < pacing_exceso_value
                )
            ), self.hf_last_day_vs_budget
        ] = control_ok                                                                                # Alerta Pacing Last Day, si esta entre -5% y 20% esta ok
        st.loc[
            st[self.hf_entrega_diaria] >= pacing_exceso_value,
            self.hf_last_day_vs_budget
        ] = control_exceso                                                                            # Alerta Pacing Last Day, si es mayor a 20% Exceso
        st.loc[
            st[self.hf_entrega_diaria] < pacing_alerta_value,
            self.hf_last_day_vs_budget
        ] = control_alerta                                                                            # Alerta Pacing Last Day, si es menor al -5% Alerta
        # Alerta Pacing Last Day - END ----------------------------------------------------------------------------------------------------------------

        # Alerta KPI - START --------------------------------------------------------------------------------------------------------------------------
        st.loc[
            (
                st[self.hf_control] == control_normal
            ) & (
                st[self.hf_kpi_total_vs_kpi_obj] > 0.00
            ), self.hf_kpi_total_pacing
        ] = control_ok                                                                                #
        st.loc[
            (
                st[self.hf_control] == control_normal
            ) & (
                st[self.hf_kpi_total_vs_kpi_obj] <= 0.00
            ), self.hf_kpi_total_pacing
        ] = control_alerta                                                                            #
        st.loc[
            (
                st[self.hf_control] == control_inverso
            ) & (
                st[self.hf_kpi] <= st[self.hf_KPI_Objetivo]
            ), self.hf_kpi_total_pacing
        ] = control_ok                                                                                #
        st.loc[
            (
                st[self.hf_control] == control_inverso
            ) & (
                st[self.hf_kpi] > st[self.hf_KPI_Objetivo]
            ), self.hf_kpi_total_pacing
        ] = control_alerta                                                                            #
        # Alerta KPI - END ----------------------------------------------------------------------------------------------------------------------------

        # Alerta KPI LastDay - START ------------------------------------------------------------------------------------------------------------------
        st.loc[
            (
                st[self.hf_control] == control_normal
            ) & (
                st[self.hf_kpi_dia_anterior] > 0.00
            ), self.hf_kpi_last_day_vs_kpi_obj
        ] = control_ok                                                                                          #
        st.loc[
            (
                st[self.hf_control] == control_normal
            ) & (
                st[self.hf_kpi_dia_anterior] <= 0.00
            ), self.hf_kpi_last_day_vs_kpi_obj
        ] = control_alerta                                                                                      #
        st.loc[
            (
                st[self.hf_control] == control_inverso
            ) & (
                st[self.hf_kpi] <= st[self.hf_KPI_Objetivo]
            ), self.hf_kpi_last_day_vs_kpi_obj
        ] = control_ok                                                                                          #
        st.loc[
            (
                st[self.hf_control] == control_inverso
            ) & (
                st[self.hf_kpi] > st[self.hf_KPI_Objetivo]
            ),
            self.hf_kpi_last_day_vs_kpi_obj
        ] = control_alerta                                                                                      #
        # Alerta KPI LastDay - END --------------------------------------------------------------------------------------------------------------------

        st[self.hf_comentarios] = ''
        st[self.hf_revisada] = ''

        st = st[[
            hf_estado,
            self.hf_line_id,
            self.hf_adv,
            self.hf_campaign,
            self.hf_dsp,
            self.hf_agencia,
            self.hf_profit,
            self.hf_pacing,
            self.hf_last_day_vs_budget,
            self.hf_kpi_total_pacing,
            self.hf_kpi_last_day_vs_kpi_obj,
            self.hn_cost,
            self.hf_revenue,
            self.hf_profit_porcentaje,
            self.hf_sm,
            self.hf_metrica_a_entregar,
            self.hf_contratado_total_a_entregar,
            self.hf_entregado_hasta_ayer,
            self.hf_contratado_por_dia,
            self.hn_date_last_day,
            self.hf_entregado_ayer_value,
            self.hf_entrega,
            self.hf_entrega_diaria,
            self.hf_KPI,
            self.hf_kpi,
            self.hf_KPI_Objetivo,
            self.hf_kpi_dia_anterior,
            self.hf_kpi_total_vs_kpi_obj,
            self.hf_dias_end,
            self.hf_trader,
            self.hf_comentarios,
            self.hf_revisada
        ]]
        st[self.hn_cost] = st[self.hn_cost].map('${:,.2f}'.format)
        st[self.hf_revenue] = st[self.hf_revenue].map('${:,.2f}'.format)
        st[self.hf_profit_porcentaje] = (st[self.hf_profit_porcentaje] * 100).map('{:,.2f}%'.format)
        st[self.hf_contratado_por_dia] = st[self.hf_contratado_por_dia].astype("int")
        st[self.hf_entrega] = (st[self.hf_entrega] * 100).map('{:,.2f}%'.format)
        st[self.hf_entrega_diaria] = (st[self.hf_entrega_diaria] * 100).map('{:,.2f}%'.format)
        st[self.hf_kpi_total_vs_kpi_obj] = (st[self.hf_kpi_total_vs_kpi_obj] * 100).map('{:,.2f}%'.format)
        st.to_csv(self.file_status_gral, index=False)


operaciones = Operaciones(
    'status_x_dia_appnexus.csv',
    'status_x_dia_dv360.csv',
    'status_general_dias.csv',
    'status_appnexus.csv',
    'status_dv360.csv',
    'status.csv',
    'Line ID',
    'Advertiser',
    'Campaign',
    'DSP',
    'Agencia',
    'Profit',
    'Pacing Teorico',
    'Pacing',
    'Entrega Ult Dia',
    'KPI Pacing',
    'kpi Ultimo dia vs Kpi Obj',
    'Revenue',
    'Costo',
    'Profit %',
    'Sell Metric',
    'Metrica a entregar',
    'Impresiones + Discrepancia',
    'Total Entregado Hasta la Fecha',
    'Contratado Por Dia',
    'Last Day Entregado ',
    'Pacing %',
    'Entrega Diaria Real vs Entrega Diaria Necesaria',
    'KPI Entregado',
    'KPI Dia Anterior',
    'kpi Total vs Kpi Obj',
    'Dias Restantes',
    'Trader',
    'Revisada',
    'Comentarios',
    'Control',
    'Revenue Last Day',
    'Sell Metric Value',
    'Start date',
    'End date',
    'KPI ',
    'KPI Objetivo',
    'Date',
    'Impressions',
    'Clicks',
    'CTR',
    'Conversions',
    'Cost',
    'Viewable Impressions',
    'Viewability',
    'Conversion Rate',
    'Completion Rate',
    'Complete Views (Video)',
    'TrueView: View Rate',
    'TrueView: Views',
    'Duracion en dias',
    'Date LastDay',
    'Impressions LastDay',
    'Clicks LastDay',
    'CTR LastDay',
    'Conversions LastDay',
    'Cost LastDay',
    'Viewable Impressions LastDay',
    'Viewability LastDay',
    'Conversion Rate LastDay',
    'Completion Rate LastDay',
    'Complete Views (Video) LastDay',
    'TrueView: View Rate LastDay',
    'TrueView: Views LastDay',
)
operaciones.yesterday_date()
operaciones.errores_files(
    'Lineas con errores_AN.csv',
    'Lineas con errores_DV360.csv',
    'tracker_no_contemplados.csv',
    'Errores.csv',
)
operaciones.concat_dsps_files()
operaciones.last_day_lineas_file(
    'last_day_x_linea.csv',
)
operaciones.calculos(
    41.51,
    28,
    0,
    'CPCV',
    'CPCV 100%',
    'TV',
    'CPE',
    'CPM',
    'CPC',
    'vCPM',
    'FINALIZO OK LA ENTREGA',
    'FINALIZO INSUFICIENTE',
    'LIVE',
    'Estado',
    'Viewability',
    'CTR',
    'Completion Rate',
    'True View Rate',
    'Clicks',
    'Impressions',
    'Alcance',
    'Reach',
    'Conversions',
    'Complete Views 100%',
    'CPC',
    'ALERTA',
    'OK',
    'EXCESO',
    'normal',
    'inverso',
    -0.05,
    0.20,
    0.70,
)
os.system('cls')
print(
    "EL PROGRAMA FINALIZO CORRECTAMENTE"
)
